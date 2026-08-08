(function () {
  const STATS_KEY = 'kiip5_stats_v1';
  const AUTH_KEY = 'kiip5_auth_v1';
  const CIRCLE = { A: '①', B: '②', C: '③', D: '④' };
  const supabaseClient = window.supabase && window.KIIP5_SUPABASE
    ? window.supabase.createClient(window.KIIP5_SUPABASE.url, window.KIIP5_SUPABASE.publishableKey)
    : null;

  const root = document.getElementById('app');

  const state = {
    screen: 'home',
    selectedSetId: (window.QUIZ_INDEX && window.QUIZ_INDEX[0]) ? window.QUIZ_INDEX[0].id : null,
    mode: 'all',
    startFrom: 1,
    session: null,
    auth: loadAuth(),
  };

  let completingSupabaseAccessToken = null;
  let quizTimerId = null;

  function loadAuth() {
    try {
      return JSON.parse(localStorage.getItem(AUTH_KEY)) || null;
    } catch (e) {
      return null;
    }
  }

  function saveAuth(auth) {
    localStorage.setItem(AUTH_KEY, JSON.stringify(auth));
  }

  function clearAuth() {
    localStorage.removeItem(AUTH_KEY);
  }

  function statsStorageKey(username = state.auth?.username) {
    return username ? `${STATS_KEY}:${username}` : `${STATS_KEY}:guest`;
  }

  async function completeSupabaseAuth(session) {
    if (!session?.access_token) return;
    if (completingSupabaseAccessToken === session.access_token) return;
    completingSupabaseAccessToken = session.access_token;
    try {
      const res = await fetch('/.netlify/functions/auth-supabase', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ accessToken: session.access_token }),
      });
      const result = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(result.error || 'Không thể hoàn tất đăng nhập.');
      state.auth = {
        token: result.token,
        username: result.username,
        displayName: result.displayName,
        role: result.role || 'user',
        provider: result.provider || 'email',
      };
      saveAuth(state.auth);
      await syncPull();
      render();
      return state.auth;
    } catch (authError) {
      console.error('Supabase session exchange failed:', authError.message);
      throw authError;
    } finally {
      if (completingSupabaseAccessToken === session.access_token) {
        completingSupabaseAccessToken = null;
      }
    }
  }

  async function hydrateSupabaseAuth() {
    if (!supabaseClient) return;
    const { data, error } = await supabaseClient.auth.getSession();
    if (error || !data.session) return;
    await completeSupabaseAuth(data.session).catch(() => {});
  }

  function listenForSupabaseAuthChanges() {
    if (!supabaseClient) return;
    supabaseClient.auth.onAuthStateChange((event, session) => {
      if (session && ['INITIAL_SESSION', 'SIGNED_IN', 'TOKEN_REFRESHED', 'USER_UPDATED'].includes(event)) {
        // Run after Supabase finishes processing the OAuth redirect and persisting the session.
        setTimeout(() => completeSupabaseAuth(session).catch(() => {}), 0);
        return;
      }
      if (event === 'SIGNED_OUT' && ['google', 'facebook', 'kakao', 'email'].includes(state.auth?.provider)) {
        clearAuth();
        state.auth = null;
        if (state.screen === 'home') render();
      }
    });
  }

  function loadStats(username = state.auth?.username) {
    try {
      const key = statsStorageKey(username);
      const saved = localStorage.getItem(key);
      if (saved) return JSON.parse(saved) || {};
      if (!username) {
        const legacy = localStorage.getItem(STATS_KEY);
        if (legacy) {
          localStorage.setItem(key, legacy);
          return JSON.parse(legacy) || {};
        }
      }
      return {};
    } catch (e) {
      return {};
    }
  }

  function saveStats(stats, username = state.auth?.username) {
    localStorage.setItem(statsStorageKey(username), JSON.stringify(stats));
  }

  function mergeStats(localStats = {}, remoteStats = {}) {
    const merged = JSON.parse(JSON.stringify(remoteStats || {}));
    Object.entries(localStats || {}).forEach(([setId, questions]) => {
      if (!merged[setId]) merged[setId] = {};
      Object.entries(questions || {}).forEach(([num, localItem]) => {
        const remoteItem = merged[setId][num];
        if (!remoteItem) {
          merged[setId][num] = { ...localItem };
          return;
        }
        const localSeen = Number(localItem.seen) || 0;
        const remoteSeen = Number(remoteItem.seen) || 0;
        const localAnsweredAt = Number(localItem.lastAnsweredAt) || 0;
        const remoteAnsweredAt = Number(remoteItem.lastAnsweredAt) || 0;
        merged[setId][num] = {
          ...remoteItem,
          ...localItem,
          seen: Math.max(localSeen, remoteSeen),
          correct: Math.max(Number(localItem.correct) || 0, Number(remoteItem.correct) || 0),
          wrong: Math.max(Number(localItem.wrong) || 0, Number(remoteItem.wrong) || 0),
          lastAnsweredAt: Math.max(localAnsweredAt, remoteAnsweredAt) || undefined,
          lastWrong: localAnsweredAt || remoteAnsweredAt
            ? (localAnsweredAt >= remoteAnsweredAt ? Boolean(localItem.lastWrong) : Boolean(remoteItem.lastWrong))
            : (localSeen >= remoteSeen ? Boolean(localItem.lastWrong) : Boolean(remoteItem.lastWrong)),
        };
      });
    });
    return merged;
  }

  let syncTimer = null;
  function syncPush() {
    if (!state.auth) return;
    const auth = state.auth;
    const stats = loadStats(auth.username);
    clearTimeout(syncTimer);
    syncTimer = setTimeout(() => {
      fetch('/.netlify/functions/sync-progress', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${auth.token}` },
        body: JSON.stringify({ stats }),
      }).catch(() => {});
    }, 800);
  }

  async function syncPull() {
    if (!state.auth) return;
    const auth = state.auth;
    try {
      const res = await fetch('/.netlify/functions/sync-progress', {
        headers: { Authorization: `Bearer ${auth.token}` },
      });
      if (res.status === 401) {
        if (state.auth?.token === auth.token) { clearAuth(); state.auth = null; }
        return;
      }
      if (!res.ok) return;
      const data = await res.json();
      if (data.stats && Object.keys(data.stats).length > 0) {
        const localStats = loadStats(auth.username);
        const mergedStats = mergeStats(localStats, data.stats);
        saveStats(mergedStats, auth.username);
        if (JSON.stringify(mergedStats) !== JSON.stringify(data.stats)) syncPush();
      } else {
        const localStats = loadStats(auth.username);
        fetch('/.netlify/functions/sync-progress', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${auth.token}` },
          body: JSON.stringify({ stats: localStats }),
        }).catch(() => {});
      }
    } catch (e) { /* offline or unreachable, keep local data */ }
  }

  function recordAnswer(setId, num, isCorrect) {
    const stats = loadStats();
    if (!stats[setId]) stats[setId] = {};
    if (!stats[setId][num]) stats[setId][num] = { seen: 0, correct: 0, wrong: 0 };
    const s = stats[setId][num];
    s.seen += 1;
    if (isCorrect) { s.correct += 1; s.lastWrong = false; }
    else { s.wrong += 1; s.lastWrong = true; }
    s.lastAnsweredAt = Date.now();
    saveStats(stats);
    syncPush();
  }

  function ensureSessionProgress(session = state.session) {
    if (!session?.setId || !Array.isArray(session.answers) || session.answers.length === 0) return;
    const stats = loadStats();
    if (!stats[session.setId]) stats[session.setId] = {};
    let changed = false;
    session.answers.forEach(answer => {
      if (stats[session.setId][answer.num]?.seen > 0) return;
      stats[session.setId][answer.num] = {
        seen: 1,
        correct: answer.correct ? 1 : 0,
        wrong: answer.correct ? 0 : 1,
        lastWrong: !answer.correct,
        lastAnsweredAt: Date.now(),
      };
      changed = true;
    });
    if (!changed) return;
    saveStats(stats);
    syncPush();
  }

  function wrongNums(setId) {
    const stats = loadStats();
    const setStats = stats[setId] || {};
    return Object.keys(setStats).filter(n => setStats[n].lastWrong).map(Number);
  }

  function setProgress(setId, questions) {
    const setStats = loadStats()[setId] || {};
    const total = questions.length;
    const validLearned = questions.filter(question => setStats[question.num]?.seen > 0).length;
    const recordedLearned = Object.values(setStats).filter(item => (item?.seen || 0) > 0).length;
    const learned = Math.min(total, Math.max(validLearned, recordedLearned));
    return {
      learned,
      total,
      pct: total > 0 ? Math.min(100, Math.round((learned / total) * 100)) : 0,
    };
  }

  function nextResumeQuestion(setId, questions) {
    const setStats = loadStats()[setId] || {};
    const seenQuestions = questions.filter(question => setStats[question.num]?.seen > 0);
    const seenNums = seenQuestions.map(question => question.num);
    if (seenNums.length === 0) return questions[0]?.num || 1;

    const latest = seenQuestions
      .map(question => ({ question, answeredAt: Number(setStats[question.num]?.lastAnsweredAt) || 0 }))
      .sort((a, b) => b.answeredAt - a.answeredAt)[0];
    if (latest?.answeredAt > 0) {
      const latestIndex = questions.findIndex(question => question.num === latest.question.num);
      if (latestIndex >= 0 && latestIndex + 1 < questions.length) return questions[latestIndex + 1].num;
      const firstUnseen = questions.find(question => !(setStats[question.num]?.seen > 0));
      return firstUnseen ? firstUnseen.num : questions[0]?.num || 1;
    }

    const recordedLearned = Object.values(setStats).filter(item => (item?.seen || 0) > 0).length;
    if (recordedLearned > seenNums.length && recordedLearned < questions.length) {
      return questions[recordedLearned]?.num || questions[0]?.num || 1;
    }
    const highestSeen = Math.max(...seenNums);
    const next = questions.find(question => question.num > highestSeen);
    if (next) return next.num;
    const firstUnseen = questions.find(question => !(setStats[question.num]?.seen > 0));
    return firstUnseen ? firstUnseen.num : questions[0]?.num || 1;
  }

  function shuffle(arr) {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function el(html) {
    const t = document.createElement('template');
    t.innerHTML = html.trim();
    return t.content.firstElementChild;
  }

  function render() {
    clearQuizTimer();
    root.innerHTML = '';
    if (state.screen === 'home') root.appendChild(renderHome());
    else if (state.screen === 'quiz') root.appendChild(renderQuiz());
    else if (state.screen === 'result') root.appendChild(renderResult());
  }

  function getSetEmoji(set) {
    const id = (set.id || '').toLowerCase();
    const title = (set.title || '').toLowerCase();
    if (id.includes('geo') || title.includes('địa lý')) return '🗺️';
    if (id.includes('hist') || title.includes('lịch sử')) return '🏛️';
    return '📝';
  }

  function overallStats() {
    const stats = loadStats();
    let seen = 0;
    let correct = 0;
    Object.keys(stats).forEach(setId => {
      Object.keys(stats[setId]).forEach(num => {
        seen += stats[setId][num].seen || 0;
        correct += stats[setId][num].correct || 0;
      });
    });
    return { seen, correct, pct: seen ? Math.round((correct / seen) * 100) : 0 };
  }

  function renderHome() {
    const wrap = el('<div></div>');

    const overall = overallStats();
    const hero = el(`
      <div class="hero">
        <div class="hero-top">
          <div class="hero-emoji">🇰🇷</div>
          <div>
            <div class="hero-title">Ôn thi KIIP cấp 5</div>
            <div class="hero-sub">Luyện trắc nghiệm mỗi ngày, tự tin đi thi!</div>
          </div>
        </div>
        ${overall.seen > 0 ? `
        <div class="hero-stats">
          <div class="hero-stat"><b>${overall.seen}</b><span>Câu đã làm</span></div>
          <div class="hero-stat"><b>${overall.pct}%</b><span>Tỉ lệ đúng</span></div>
          <div class="hero-stat"><b>${(window.QUIZ_INDEX || []).length}</b><span>Bộ đề</span></div>
        </div>` : ''}
      </div>
    `);
    wrap.appendChild(hero);

    wrap.appendChild(renderAccountBar());
    wrap.appendChild(renderSupportButtons());
    wrap.appendChild(renderFeedbackButton());

    wrap.appendChild(el('<div class="section-label">Chọn đề</div>'));
    const setsWrap = el('<div></div>');
    (window.QUIZ_INDEX || []).forEach(set => {
      const data = window.QUIZ_DATA[set.id];
      const selected = set.id === state.selectedSetId;
      const learning = setProgress(set.id, data.questions);
      const progress = state.auth ? learning : null;
      const card = el(`
        <button type="button" class="card set-card ${selected ? 'selected' : ''}">
          <div class="set-card-main">
            <div class="set-emoji">${getSetEmoji(set)}</div>
            <div class="set-card-content">
              <div class="title">${escapeHtml(set.title)}</div>
              <div class="meta">${data.questions.length} câu${data.durationMinutes ? ` · ${data.durationMinutes} phút` : ''}</div>
              ${progress ? `
                <div class="set-progress-row">
                  <span>Đã học ${progress.learned}/${progress.total} câu</span>
                  <strong>${progress.pct}%</strong>
                </div>
                <div class="set-progress-bar" role="progressbar" aria-label="Tiến độ ${escapeHtml(set.title)}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="${progress.pct}">
                  <span style="width:${progress.pct}%"></span>
                </div>
              ` : ''}
            </div>
          </div>
          ${selected ? '<div class="set-check">✓</div>' : ''}
        </button>
      `);
      card.addEventListener('click', () => {
        state.selectedSetId = set.id;
        state.mode = 'all';
        state.startFrom = nextResumeQuestion(set.id, data.questions);
        render();
      });
      setsWrap.appendChild(card);
      if (selected) {
        const resumeFrom = nextResumeQuestion(set.id, data.questions);
        const quickActions = el(`
          <div class="set-quick-actions">
            <button type="button" class="primary set-resume-button">Học tiếp từ câu ${resumeFrom} →</button>
            <button type="button" class="secondary set-restart-button">↺ Học lại từ câu 1</button>
            <div class="set-custom-start">
              <label for="custom-start-${escapeHtml(set.id)}">Chọn câu bắt đầu</label>
              <div>
                <input id="custom-start-${escapeHtml(set.id)}" type="number" min="1" max="${data.questions.length}" value="${resumeFrom}" inputmode="numeric">
                <button type="button" class="secondary set-custom-start-button">Bắt đầu</button>
              </div>
            </div>
          </div>
        `);
        quickActions.querySelector('.set-resume-button').addEventListener('click', () => {
          state.selectedSetId = set.id;
          state.mode = 'all';
          state.startFrom = resumeFrom;
          startQuiz();
        });
        quickActions.querySelector('.set-restart-button').addEventListener('click', () => {
          state.selectedSetId = set.id;
          state.mode = 'all';
          state.startFrom = 1;
          startQuiz();
        });
        const customInput = quickActions.querySelector('.set-custom-start input');
        quickActions.querySelector('.set-custom-start-button').addEventListener('click', () => {
          let chosen = parseInt(customInput.value, 10);
          if (!chosen || chosen < 1) chosen = 1;
          if (chosen > data.questions.length) chosen = data.questions.length;
          customInput.value = chosen;
          state.selectedSetId = set.id;
          state.mode = 'all';
          state.startFrom = chosen;
          startQuiz();
        });
        setsWrap.appendChild(quickActions);
      }
    });
    wrap.appendChild(setsWrap);

    const wrongCount = wrongNums(state.selectedSetId).length;
    const modes = [
      { id: 'all', emoji: '📋', title: 'Làm toàn bộ (theo thứ tự)', meta: 'Đi từ câu 1 đến câu cuối' },
      { id: 'shuffle', emoji: '🔀', title: 'Làm toàn bộ (trộn ngẫu nhiên)', meta: 'Thứ tự câu hỏi được xáo trộn' },
      { id: 'wrong', emoji: '🎯', title: 'Chỉ ôn câu từng làm sai', meta: wrongCount > 0 ? `${wrongCount} câu` : 'Chưa có câu sai nào được ghi nhận' },
    ];

    wrap.appendChild(el('<div class="section-label">Chế độ ôn tập</div>'));
    const modeWrap = el('<div class="mode-grid"></div>');
    modes.forEach(m => {
      const disabled = m.id === 'wrong' && wrongCount === 0;
      const opt = el(`
        <button type="button" class="mode-option ${state.mode === m.id ? 'selected' : ''}" style="${disabled ? 'opacity:.5;pointer-events:none;' : ''}" ${disabled ? 'disabled' : ''}>
          <div class="mode-emoji">${m.emoji}</div>
          <div>
            <div class="title">${m.title}</div>
            <div class="meta">${m.meta}</div>
          </div>
        </button>
      `);
      opt.addEventListener('click', () => { state.mode = m.id; render(); });
      modeWrap.appendChild(opt);
    });
    wrap.appendChild(modeWrap);

    const startBtn = el('<button class="primary">Bắt đầu</button>');
    startBtn.addEventListener('click', startQuiz);
    wrap.appendChild(startBtn);

    wrap.appendChild(el('<div class="footer-note">Tiến trình được lưu trên trình duyệt này.</div>'));
    return wrap;
  }

  function renderAccountBar() {
    if (state.auth) {
      const bar = el(`
        <div class="feedback-entry" style="cursor:default;">
          <span class="feedback-entry-icon" aria-hidden="true">👋</span>
          <span><strong>Xin chào, ${escapeHtml(state.auth.displayName || state.auth.username)}</strong><small>Tiến trình của bạn đang được đồng bộ</small></span>
        </div>
      `);
      const accountActions = el('<span style="display:flex;align-items:center;gap:12px;margin-left:auto;"></span>');
      if (state.auth.role === 'admin') {
        const adminBtn = el('<button type="button" class="link-btn">관리자</button>');
        adminBtn.addEventListener('click', () => { window.location.href = '/admin.html'; });
        accountActions.appendChild(adminBtn);
      }
      const logoutBtn = el('<button type="button" class="link-btn">Đăng xuất</button>');
      bar.style.cursor = 'default';
      accountActions.appendChild(logoutBtn);
      bar.appendChild(accountActions);
      logoutBtn.addEventListener('click', async () => {
        if (['google', 'facebook', 'kakao', 'email'].includes(state.auth?.provider) && supabaseClient) await supabaseClient.auth.signOut({ scope: 'local' });
        clearAuth();
        state.auth = null;
        render();
      });
      return bar;
    }
    const button = el(`
      <button type="button" class="feedback-entry">
        <span class="feedback-entry-icon" aria-hidden="true">👤</span>
        <span><strong>Đăng nhập</strong><small>Lưu tiến trình và đồng bộ giữa các thiết bị</small></span>
        <span class="feedback-arrow" aria-hidden="true">›</span>
      </button>
    `);
    button.addEventListener('click', () => showAuthModal('login'));
    return button;
  }

  function showEmailConfirmationModal() {
    const modal = el(`
      <div class="support-modal" role="dialog" aria-modal="true" aria-label="Đã gửi email xác nhận">
        <div class="support-backdrop"></div>
        <div class="support-dialog feedback-dialog">
          <button type="button" class="support-close" aria-label="Đóng">×</button>
          <div class="feedback-modal-icon" aria-hidden="true">✉️</div>
          <div class="support-modal-title">Đã gửi email xác nhận</div>
          <div class="feedback-intro">Hãy mở email và bấm liên kết để kích hoạt tài khoản.</div>
          <button type="button" class="primary email-confirmation-close">Đã hiểu</button>
        </div>
      </div>
    `);
    const close = () => {
      document.removeEventListener('keydown', onKeydown);
      modal.remove();
    };
    const onKeydown = event => { if (event.key === 'Escape') close(); };
    modal.querySelector('.support-close').addEventListener('click', close);
    modal.querySelector('.support-backdrop').addEventListener('click', close);
    modal.querySelector('.email-confirmation-close').addEventListener('click', close);
    document.addEventListener('keydown', onKeydown);
    document.body.appendChild(modal);
    modal.querySelector('.email-confirmation-close').focus();
  }

  function showAuthModal(initialMode) {
    let mode = initialMode;
    const modal = el(`
      <div class="support-modal" role="dialog" aria-modal="true" aria-label="Đăng nhập">
        <div class="support-backdrop"></div>
        <div class="support-dialog feedback-dialog">
          <button type="button" class="support-close" aria-label="Đóng">×</button>
          <div class="feedback-modal-icon" aria-hidden="true">👤</div>
          <div class="support-modal-title auth-title"></div>
          <div class="feedback-intro">Lưu tiến trình ôn tập và đồng bộ giữa điện thoại, máy tính.</div>
          <form class="feedback-form auth-form">
            <label class="auth-display-name-label" style="display:none;">
              Tên hiển thị <span>(không bắt buộc)</span>
              <input name="displayName" type="text" maxlength="60" autocomplete="nickname" placeholder="Ví dụ: Minh">
            </label>
            <label class="auth-username-label">
              <span class="auth-username-text">Tên đăng nhập</span>
              <input name="username" type="text" maxlength="20" autocomplete="username" placeholder="3-20 ký tự, chữ thường/số/gạch dưới" required>
            </label>
            <label class="auth-email-label" style="display:none;">
              Email
              <input name="email" type="email" maxlength="254" autocomplete="email" placeholder="ten@example.com">
            </label>
            <label>
              Mật khẩu
              <input name="password" type="password" maxlength="100" autocomplete="current-password" placeholder="Ít nhất 6 ký tự" required>
            </label>
            <div class="feedback-status" role="status" aria-live="polite"></div>
            <button type="submit" class="primary auth-submit"></button>
          </form>
          <div class="auth-divider"><span>hoặc</span></div>
          <button type="button" class="google-auth-button">
            <span class="google-g" aria-hidden="true">G</span>
            Đăng nhập bằng Google
          </button>
          <button type="button" class="facebook-auth-button">
            <span class="facebook-f" aria-hidden="true">f</span>
            Đăng nhập bằng Facebook
          </button>
          <button type="button" class="kakao-auth-button">
            <span class="kakao-symbol" aria-hidden="true">💬</span>
            Đăng nhập bằng Kakao
          </button>
          <button type="button" class="link-btn auth-toggle" style="display:block;margin:10px auto 0;"></button>
        </div>
      </div>
    `);

    const titleEl = modal.querySelector('.auth-title');
    const submitBtn = modal.querySelector('.auth-submit');
    const toggleBtn = modal.querySelector('.auth-toggle');
    const displayNameLabel = modal.querySelector('.auth-display-name-label');
    const emailLabel = modal.querySelector('.auth-email-label');
    const emailInput = modal.querySelector('input[name="email"]');
    const usernameInput = modal.querySelector('input[name="username"]');
    const usernameText = modal.querySelector('.auth-username-text');
    const status = modal.querySelector('.feedback-status');
    const googleBtn = modal.querySelector('.google-auth-button');
    const facebookBtn = modal.querySelector('.facebook-auth-button');
    const kakaoBtn = modal.querySelector('.kakao-auth-button');

    const applyMode = () => {
      status.textContent = '';
      status.className = 'feedback-status';
      if (mode === 'login') {
        titleEl.textContent = 'Đăng nhập';
        submitBtn.textContent = 'Đăng nhập';
        toggleBtn.textContent = 'Chưa có tài khoản? Đăng ký ngay';
        displayNameLabel.style.display = 'none';
        emailLabel.style.display = 'none';
        emailInput.required = false;
        usernameText.textContent = 'Tên đăng nhập hoặc email';
        usernameInput.maxLength = 254;
        usernameInput.placeholder = 'Tên đăng nhập cũ hoặc email';
      } else {
        titleEl.textContent = 'Đăng ký tài khoản';
        submitBtn.textContent = 'Đăng ký';
        toggleBtn.textContent = 'Đã có tài khoản? Đăng nhập';
        displayNameLabel.style.display = 'block';
        emailLabel.style.display = 'block';
        emailInput.required = true;
        usernameText.textContent = 'Tên đăng nhập';
        usernameInput.maxLength = 20;
        usernameInput.placeholder = '3-20 ký tự, chữ thường/số/gạch dưới';
      }
    };
    applyMode();
    toggleBtn.addEventListener('click', () => { mode = mode === 'login' ? 'register' : 'login'; applyMode(); });
    googleBtn.addEventListener('click', async () => {
      if (!supabaseClient) {
        status.className = 'feedback-status error';
        status.textContent = 'Đăng nhập Google chưa tải được. Vui lòng tải lại trang.';
        return;
      }
      googleBtn.disabled = true;
      status.textContent = 'Đang chuyển tới Google...';
      const { error } = await supabaseClient.auth.signInWithOAuth({
        provider: 'google',
        options: { redirectTo: `${window.location.origin}/` },
      });
      if (error) {
        googleBtn.disabled = false;
        status.className = 'feedback-status error';
        status.textContent = error.message || 'Không thể đăng nhập bằng Google.';
      }
    });
    facebookBtn.addEventListener('click', async () => {
      if (!supabaseClient) {
        status.className = 'feedback-status error';
        status.textContent = 'Đăng nhập Facebook chưa tải được. Vui lòng tải lại trang.';
        return;
      }
      facebookBtn.disabled = true;
      status.textContent = 'Đang chuyển tới Facebook...';
      const { error } = await supabaseClient.auth.signInWithOAuth({
        provider: 'facebook',
        options: { redirectTo: `${window.location.origin}/` },
      });
      if (error) {
        facebookBtn.disabled = false;
        status.className = 'feedback-status error';
        status.textContent = error.message || 'Không thể đăng nhập bằng Facebook.';
      }
    });
    kakaoBtn.addEventListener('click', async () => {
      if (!supabaseClient) {
        status.className = 'feedback-status error';
        status.textContent = 'Đăng nhập Kakao chưa tải được. Vui lòng tải lại trang.';
        return;
      }
      kakaoBtn.disabled = true;
      status.textContent = 'Đang chuyển tới Kakao...';
      const { error } = await supabaseClient.auth.signInWithOAuth({
        provider: 'kakao',
        options: { redirectTo: `${window.location.origin}/` },
      });
      if (error) {
        kakaoBtn.disabled = false;
        status.className = 'feedback-status error';
        status.textContent = error.message || 'Không thể đăng nhập bằng Kakao.';
      }
    });

    const close = () => {
      document.removeEventListener('keydown', onKeydown);
      modal.remove();
    };
    const onKeydown = event => { if (event.key === 'Escape') close(); };
    modal.querySelector('.support-close').addEventListener('click', close);
    modal.querySelector('.support-backdrop').addEventListener('click', close);
    document.addEventListener('keydown', onKeydown);
    document.body.appendChild(modal);

    const form = modal.querySelector('.auth-form');
    form.addEventListener('submit', async event => {
      event.preventDefault();
      const formData = new FormData(form);
      const username = String(formData.get('username') || '').trim();
      const password = String(formData.get('password') || '');
      const displayName = String(formData.get('displayName') || '').trim();
      const email = String(formData.get('email') || '').trim().toLowerCase();

      submitBtn.disabled = true;
      submitBtn.textContent = mode === 'login' ? 'Đang đăng nhập...' : 'Đang đăng ký...';
      status.textContent = '';

      try {
        if (mode === 'register') {
          if (!supabaseClient) throw new Error('Đăng ký email chưa tải được. Vui lòng tải lại trang.');
          if (!/^[a-z0-9_]{3,20}$/.test(username)) throw new Error('Tên đăng nhập phải dài 3-20 ký tự, chỉ gồm chữ thường/số/gạch dưới.');
          if (!email || !email.includes('@')) throw new Error('Vui lòng nhập email hợp lệ.');
          const { data, error } = await supabaseClient.auth.signUp({
            email,
            password,
            options: {
              emailRedirectTo: `${window.location.origin}/`,
              data: { username, display_name: displayName || username },
            },
          });
          if (error) throw error;
          if (data.session) throw new Error('Máy chủ chưa bật xác nhận email. Tài khoản chưa được kích hoạt.');
          form.reset();
          close();
          showEmailConfirmationModal();
          return;
        }

        if (username.includes('@')) {
          if (!supabaseClient) throw new Error('Đăng nhập email chưa tải được. Vui lòng tải lại trang.');
          const { data, error } = await supabaseClient.auth.signInWithPassword({ email: username.toLowerCase(), password });
          if (error) throw error;
          await completeSupabaseAuth(data.session);
          close();
          return;
        }

        const endpoint = mode === 'login' ? '/.netlify/functions/auth-login' : '/.netlify/functions/auth-register';
        const payload = { username, password };
        const res = await fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
        });
        const result = await res.json().catch(() => ({}));
        if (!res.ok) throw new Error(result.error || 'Có lỗi xảy ra.');

        state.auth = { token: result.token, username: result.username, displayName: result.displayName, role: result.role || 'user' };
        saveAuth(state.auth);
        status.className = 'feedback-status success';
        status.textContent = 'Thành công! Đang đồng bộ dữ liệu...';
        await syncPull();
        setTimeout(() => { close(); render(); }, 600);
      } catch (error) {
        submitBtn.disabled = false;
        submitBtn.textContent = mode === 'login' ? 'Đăng nhập' : 'Đăng ký';
        status.className = 'feedback-status error';
        status.textContent = error.message || 'Có lỗi xảy ra. Vui lòng thử lại.';
      }
    });
    modal.querySelector('input[name="username"]').focus();
  }

  function renderSupportButtons() {
    const support = el(`
      <section class="support-section" aria-label="Ủng hộ admin">
        <div class="support-heading">Ủng hộ admin</div>
        <div class="support-actions">
          <button type="button" class="support-button" data-support="coffee">
            <span class="support-icon" aria-hidden="true">☕</span>
            <span><strong>Mời ly cà phê</strong><small>10.000₫</small></span>
          </button>
          <button type="button" class="support-button" data-support="pho">
            <span class="support-icon" aria-hidden="true">🍜</span>
            <span><strong>Mời tô phở</strong><small>20.000₫</small></span>
          </button>
        </div>
      </section>
    `);
    support.querySelector('[data-support="coffee"]').addEventListener('click', () => {
      showSupportQr('Mời admin ly cà phê', '10.000₫', 'assets/qr-coffee-10k.jpg');
    });
    support.querySelector('[data-support="pho"]').addEventListener('click', () => {
      showSupportQr('Mời admin tô phở', '20.000₫', 'assets/qr-pho-20k.jpg');
    });
    return support;
  }

  function showSupportQr(title, amount, imageSrc) {
    const modal = el(`
      <div class="support-modal" role="dialog" aria-modal="true" aria-label="${escapeHtml(title)}">
        <div class="support-backdrop"></div>
        <div class="support-dialog">
          <button type="button" class="support-close" aria-label="Đóng">×</button>
          <div class="support-modal-icon" aria-hidden="true">${amount === '10.000₫' ? '☕' : '🍜'}</div>
          <div class="support-modal-title">${escapeHtml(title)}</div>
          <div class="support-amount">${escapeHtml(amount)}</div>
          <img class="support-qr" src="${imageSrc}" alt="Mã QR ${escapeHtml(title)} ${escapeHtml(amount)}">
          <div class="support-tip">Mở ứng dụng ngân hàng và quét mã QR</div>
        </div>
      </div>
    `);
    const close = () => {
      document.removeEventListener('keydown', onKeydown);
      modal.remove();
    };
    const onKeydown = event => { if (event.key === 'Escape') close(); };
    modal.querySelector('.support-close').addEventListener('click', close);
    modal.querySelector('.support-backdrop').addEventListener('click', close);
    document.addEventListener('keydown', onKeydown);
    document.body.appendChild(modal);
    modal.querySelector('.support-close').focus();
  }

  function renderFeedbackButton() {
    const button = el(`
      <button type="button" class="feedback-entry">
        <span class="feedback-entry-icon" aria-hidden="true">💬</span>
        <span><strong>Góp ý cải thiện ứng dụng</strong><small>Báo lỗi câu hỏi hoặc gửi đề xuất cho admin</small></span>
        <span class="feedback-arrow" aria-hidden="true">›</span>
      </button>
    `);
    button.addEventListener('click', showFeedbackModal);
    return button;
  }

  function renderQuizQuickActions(questionNum, setTitle) {
    const actions = el(`
      <div class="quiz-quick-actions" aria-label="Góp ý và ủng hộ admin">
        <button type="button" data-action="feedback">💬 <span>Góp ý câu ${questionNum}</span></button>
        <button type="button" data-action="coffee">☕ <span>Cà phê</span></button>
        <button type="button" data-action="pho">🍜 <span>Tô phở</span></button>
      </div>
    `);
    actions.querySelector('[data-action="feedback"]').addEventListener('click', () => {
      showFeedbackModal(`Góp ý về câu ${questionNum} - bộ đề "${setTitle}": `);
    });
    actions.querySelector('[data-action="coffee"]').addEventListener('click', () => {
      showSupportQr('Mời admin ly cà phê', '10.000₫', 'assets/qr-coffee-10k.jpg');
    });
    actions.querySelector('[data-action="pho"]').addEventListener('click', () => {
      showSupportQr('Mời admin tô phở', '20.000₫', 'assets/qr-pho-20k.jpg');
    });
    return actions;
  }

  function showFeedbackModal(initialMessage = '') {
    const modal = el(`
      <div class="support-modal" role="dialog" aria-modal="true" aria-label="Góp ý cải thiện ứng dụng">
        <div class="support-backdrop"></div>
        <div class="support-dialog feedback-dialog">
          <button type="button" class="support-close" aria-label="Đóng">×</button>
          <div class="feedback-modal-icon" aria-hidden="true">💬</div>
          <div class="support-modal-title">Góp ý cải thiện ứng dụng</div>
          <div class="feedback-intro">Ý kiến của bạn sẽ được gửi trực tiếp đến admin.</div>
          <form class="feedback-form">
            <label>
              Tên của bạn <span>(không bắt buộc)</span>
              <input name="name" type="text" maxlength="80" autocomplete="name" placeholder="Nhập tên hoặc biệt danh">
            </label>
            <label>
              Nội dung góp ý
              <textarea name="message" maxlength="1500" rows="6" required placeholder="Ví dụ: Câu 16 bị sai, đề xuất thêm chức năng..."></textarea>
            </label>
            <input class="feedback-honeypot" name="website" type="text" tabindex="-1" autocomplete="off" aria-hidden="true">
            <div class="feedback-status" role="status" aria-live="polite"></div>
            <button type="submit" class="primary feedback-submit">Gửi góp ý</button>
          </form>
        </div>
      </div>
    `);
    const close = () => {
      document.removeEventListener('keydown', onKeydown);
      modal.remove();
    };
    const onKeydown = event => { if (event.key === 'Escape') close(); };
    modal.querySelector('.support-close').addEventListener('click', close);
    modal.querySelector('.support-backdrop').addEventListener('click', close);
    document.addEventListener('keydown', onKeydown);
    document.body.appendChild(modal);

    const form = modal.querySelector('.feedback-form');
    form.elements.message.value = initialMessage;
    const status = modal.querySelector('.feedback-status');
    const submit = modal.querySelector('.feedback-submit');
    form.addEventListener('submit', async event => {
      event.preventDefault();
      const formData = new FormData(form);
      const message = String(formData.get('message') || '').trim();
      if (message.length < 5) {
        status.className = 'feedback-status error';
        status.textContent = 'Vui lòng nhập nội dung góp ý rõ hơn.';
        return;
      }
      submit.disabled = true;
      submit.textContent = 'Đang gửi...';
      status.textContent = '';
      try {
        const response = await fetch('/.netlify/functions/feedback', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name: String(formData.get('name') || '').trim(),
            message,
            website: String(formData.get('website') || ''),
            page: location.href,
          }),
        });
        const result = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(result.error || 'Không thể gửi góp ý.');
        form.reset();
        status.className = 'feedback-status success';
        status.textContent = 'Cảm ơn bạn! Góp ý đã được gửi đến admin.';
        submit.textContent = 'Đã gửi';
        setTimeout(close, 1800);
      } catch (error) {
        status.className = 'feedback-status error';
        status.textContent = error.message || 'Có lỗi xảy ra. Vui lòng thử lại.';
        submit.disabled = false;
        submit.textContent = 'Gửi lại';
      }
    });
    modal.querySelector('textarea').focus();
  }

  function startQuiz() {
    const data = window.QUIZ_DATA[state.selectedSetId];
    let questions = data.questions.slice();
    let startIndex = 0;
    if (state.mode === 'wrong') {
      const nums = new Set(wrongNums(state.selectedSetId));
      questions = questions.filter(q => nums.has(q.num));
      questions = shuffle(questions);
    } else if (state.mode === 'shuffle') {
      questions = shuffle(questions);
    } else if (state.mode === 'all' && state.startFrom > 1) {
      const selectedIndex = questions.findIndex(q => q.num === state.startFrom);
      startIndex = selectedIndex >= 0 ? selectedIndex : Math.min(state.startFrom - 1, questions.length - 1);
    }
    if (questions.length === 0) return;
    state.session = {
      setId: state.selectedSetId,
      setTitle: data.title,
      total: data.questions.length,
      questions,
      index: startIndex,
      answers: [],
      durationMinutes: Number(data.durationMinutes) || 0,
      timerStartedAt: data.durationMinutes ? Date.now() : null,
      timerEndsAt: data.durationMinutes ? Date.now() + Number(data.durationMinutes) * 60 * 1000 : null,
    };
    state.screen = 'quiz';
    render();
  }

  function renderQuiz() {
    const s = state.session;
    const q = s.questions[s.index];
    const wrap = el('<div></div>');

    const topBar = el('<div class="top-bar"></div>');
    const exitBtn = el('<button class="link-btn">← Thoát</button>');
    exitBtn.addEventListener('click', () => {
      if (confirm('Thoát bài làm hiện tại?')) { state.screen = 'home'; render(); }
    });
    topBar.appendChild(exitBtn);
    topBar.appendChild(el(`<div class="meta" style="color:var(--muted);font-size:13px">${escapeHtml(s.setTitle)}</div>`));
    wrap.appendChild(topBar);
    if (s.timerEndsAt) {
      const timer = el(`
        <div class="quiz-timer" role="timer" aria-live="off" aria-label="Thời gian làm bài còn lại">
          <span>⏱️ 필기시험 · Còn lại</span>
          <strong>--:--</strong>
        </div>
      `);
      wrap.appendChild(timer);
      startQuizTimer(timer, s);
    }
    wrap.appendChild(renderQuizQuickActions(q.num, s.setTitle));

    const pct = Math.round((s.index / s.questions.length) * 100);
    wrap.appendChild(el(`
      <div class="progress-row"><span>Câu ${q.num}/${s.total}</span><span>${s.answers.filter(a => a.correct).length} đúng</span></div>
    `));
    wrap.appendChild(el(`<div class="progress-bar"><div style="width:${pct}%"></div></div>`));

    const card = el('<div class="card"></div>');
    card.appendChild(el(`<div class="stem">${escapeHtml(String(q.num) + '. ' + formatQuestionStem(q.stem))}</div>`));

    const optsWrap = el('<div class="options"></div>');
    let currentAnswer = s.answers.find(answer => answer.num === q.num) || null;
    let locked = Boolean(currentAnswer);
    let nav;

    const showExplanation = answer => {
      if (!q.explanation || card.querySelector('.explain-box')) return;
      const emoji = answer.correct ? '✅' : '💡';
      const label = answer.correct ? 'Vì sao đúng' : 'Giải thích';
      const box = el(`
        <div class="explain-box">
          <div class="explain-title"><span aria-hidden="true">${emoji}</span> ${label}</div>
          <div class="explain-text">${escapeHtml(q.explanation)}</div>
        </div>
      `);
      if (nav) card.insertBefore(box, nav);
      else card.appendChild(box);
    };

    const showAnswerState = answer => {
      Array.from(optsWrap.children).forEach((child, index) => {
        child.classList.add('locked');
        const label = q.options[index].label;
        if (label === q.correct) child.classList.add('correct');
        if (!answer.correct && label === answer.chosen) child.classList.add('wrong');
      });
      showExplanation(answer);
    };

    q.options.forEach(opt => {
      const optEl = el(`
        <button type="button" class="option">
          <div class="label">${CIRCLE[opt.label] || opt.label}</div>
          <div>${escapeHtml(opt.text)}</div>
        </button>
      `);
      optEl.addEventListener('click', () => {
        if (locked) return;
        locked = true;
        const isCorrect = opt.label === q.correct;
        recordAnswer(s.setId, q.num, isCorrect);
        currentAnswer = { num: q.num, chosen: opt.label, correct: isCorrect };
        s.answers.push(currentAnswer);
        showAnswerState(currentAnswer);
      });
      optsWrap.appendChild(optEl);
    });
    card.appendChild(optsWrap);

    if (currentAnswer) showAnswerState(currentAnswer);

    nav = el(`
      <div class="quiz-nav">
        <button type="button" class="secondary quiz-prev" ${s.index === 0 ? 'disabled' : ''}>← Câu trước</button>
        <button type="button" class="primary quiz-next">${s.index + 1 < s.questions.length ? 'Câu tiếp →' : 'Xem kết quả'}</button>
      </div>
    `);
    nav.querySelector('.quiz-prev').addEventListener('click', () => {
      if (s.index === 0) return;
      s.index -= 1;
      render();
    });
    nav.querySelector('.quiz-next').addEventListener('click', () => {
      if (s.index + 1 < s.questions.length) {
        s.index += 1;
        render();
      } else {
        ensureSessionProgress(s);
        state.screen = 'result';
        render();
      }
    });
    card.appendChild(nav);

    wrap.appendChild(card);
    return wrap;
  }

  function scoreReaction(pct) {
    if (pct >= 90) return { emoji: '🏆', msg: 'Xuất sắc! Bạn đã sẵn sàng đi thi!' };
    if (pct >= 70) return { emoji: '🎉', msg: 'Rất tốt! Chỉ cần ôn thêm chút nữa.' };
    if (pct >= 50) return { emoji: '💪', msg: 'Khá ổn, cố gắng luyện thêm nhé!' };
    return { emoji: '📚', msg: 'Đừng nản, luyện thêm vài lần nữa là ăn chắc!' };
  }

  function renderResult() {
    const s = state.session;
    const total = s.answers.length;
    const correctCount = s.answers.filter(a => a.correct).length;
    const pct = total ? Math.round((correctCount / total) * 100) : 0;
    const reaction = scoreReaction(pct);

    const wrap = el('<div></div>');
    wrap.appendChild(el('<h1>Kết quả</h1>'));
    const card = el('<div class="card score-hero"></div>');
    card.appendChild(el(`<div class="score-emoji">${reaction.emoji}</div>`));
    card.appendChild(el(`<div class="score-big">${correctCount}/${total}</div>`));
    card.appendChild(el(`<div class="score-sub">${pct}% đúng</div>`));
    card.appendChild(el(`<div class="score-msg">${reaction.msg}</div>`));
    wrap.appendChild(card);

    const retryBtn = el('<button class="primary">Làm lại toàn bộ đề này</button>');
    retryBtn.addEventListener('click', () => { state.mode = 'all'; startQuiz(); });
    wrap.appendChild(retryBtn);

    const wrongList = s.answers.filter(a => !a.correct);
    if (wrongList.length > 0) {
      const wrongBtn = el('<button class="secondary">Chỉ ôn lại câu sai vừa làm</button>');
      wrongBtn.addEventListener('click', () => {
        const data = window.QUIZ_DATA[s.setId];
        const nums = new Set(wrongList.map(w => w.num));
        state.session = {
          setId: s.setId,
          setTitle: s.setTitle,
          total: data.questions.length,
          questions: shuffle(data.questions.filter(q => nums.has(q.num))),
          index: 0,
          answers: [],
        };
        state.screen = 'quiz';
        render();
      });
      wrap.appendChild(wrongBtn);
    }

    const homeBtn = el('<button class="secondary">Về trang chủ</button>');
    homeBtn.addEventListener('click', () => {
      ensureSessionProgress(s);
      state.selectedSetId = s.setId;
      state.startFrom = nextResumeQuestion(s.setId, window.QUIZ_DATA[s.setId].questions);
      state.screen = 'home';
      render();
    });
    wrap.appendChild(homeBtn);

    if (wrongList.length > 0) {
      wrap.appendChild(el('<h1 style="font-size:18px;margin-top:28px;">Xem lại câu sai</h1>'));
      const data = window.QUIZ_DATA[s.setId];
      wrongList.forEach(w => {
        const q = data.questions.find(x => x.num === w.num);
        const chosenOpt = q.options.find(o => o.label === w.chosen);
        const correctOpt = q.options.find(o => o.label === q.correct);
        const item = el(`
          <div class="review-item">
            <div class="q-num">Câu ${q.num}</div>
            <div class="q-stem">${escapeHtml(formatQuestionStem(q.stem))}</div>
            <div class="ans-line wrong">Bạn chọn: ${CIRCLE[chosenOpt.label]} ${escapeHtml(chosenOpt.text)}</div>
            <div class="ans-line correct">Đáp án đúng: ${CIRCLE[correctOpt.label]} ${escapeHtml(correctOpt.text)}</div>
          </div>
        `);
        if (q.explanation) {
          item.appendChild(el(`
            <div class="explain-box">
              <div class="explain-title"><span aria-hidden="true">💡</span> Giải thích</div>
              <div class="explain-text">${escapeHtml(q.explanation)}</div>
            </div>
          `));
        }
        wrap.appendChild(item);
      });
    }

    return wrap;
  }

  function formatQuestionStem(stem) {
    return String(stem || '')
      .replace(/<보기>[ \t]*(?=ㄱ[.．])/g, '<보기>\n')
      .replace(/[^\n](?=[ㄱㄴㄷㄹㅁ][.．][ \t]*)/g, match => `${match}\n`);
  }

  function clearQuizTimer() {
    if (!quizTimerId) return;
    clearInterval(quizTimerId);
    quizTimerId = null;
  }

  function startQuizTimer(element, session) {
    const value = element.querySelector('strong');
    const update = () => {
      const remainingMs = Math.max(0, session.timerEndsAt - Date.now());
      const totalSeconds = Math.ceil(remainingMs / 1000);
      const minutes = Math.floor(totalSeconds / 60);
      const seconds = totalSeconds % 60;
      value.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
      element.classList.toggle('warning', totalSeconds > 300 && totalSeconds <= 600);
      element.classList.toggle('danger', totalSeconds <= 300);
      if (totalSeconds === 0) {
        element.classList.add('expired');
        element.querySelector('span').textContent = '⏰ 필기시험 · Hết giờ';
        session.timeExpired = true;
        clearQuizTimer();
      }
    };
    update();
    if (!session.timeExpired) quizTimerId = setInterval(update, 1000);
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function trackVisit() {
    try {
      fetch('/.netlify/functions/track', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ page: location.pathname, referrer: document.referrer }),
        keepalive: true,
      }).catch(() => {});
    } catch (e) { /* ignore */ }
  }

  listenForSupabaseAuthChanges();
  render();
  trackVisit();
  hydrateSupabaseAuth();
  if (state.auth) {
    syncPull().then(() => { if (state.screen === 'home') render(); });
  }
})();
