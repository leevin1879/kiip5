(function () {
  const STATS_KEY = 'kiip5_stats_v1';
  const CIRCLE = { A: '①', B: '②', C: '③', D: '④' };

  const root = document.getElementById('app');

  const state = {
    screen: 'home',
    selectedSetId: (window.QUIZ_INDEX && window.QUIZ_INDEX[0]) ? window.QUIZ_INDEX[0].id : null,
    mode: 'all',
    startFrom: 1,
    session: null,
  };

  function loadStats() {
    try {
      return JSON.parse(localStorage.getItem(STATS_KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function saveStats(stats) {
    localStorage.setItem(STATS_KEY, JSON.stringify(stats));
  }

  function recordAnswer(setId, num, isCorrect) {
    const stats = loadStats();
    if (!stats[setId]) stats[setId] = {};
    if (!stats[setId][num]) stats[setId][num] = { seen: 0, correct: 0, wrong: 0 };
    const s = stats[setId][num];
    s.seen += 1;
    if (isCorrect) { s.correct += 1; s.lastWrong = false; }
    else { s.wrong += 1; s.lastWrong = true; }
    saveStats(stats);
  }

  function wrongNums(setId) {
    const stats = loadStats();
    const setStats = stats[setId] || {};
    return Object.keys(setStats).filter(n => setStats[n].lastWrong).map(Number);
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
    root.innerHTML = '';
    if (state.screen === 'home') root.appendChild(renderHome());
    else if (state.screen === 'quiz') root.appendChild(renderQuiz());
    else if (state.screen === 'result') root.appendChild(renderResult());
  }

  function renderHome() {
    const wrap = el('<div></div>');
    wrap.appendChild(el('<h1>Ôn thi KIIP cấp 5</h1>'));
    wrap.appendChild(el('<div class="subtitle">Chọn đề và chế độ ôn tập</div>'));

    const setsWrap = el('<div></div>');
    (window.QUIZ_INDEX || []).forEach(set => {
      const data = window.QUIZ_DATA[set.id];
      const card = el(`
        <button type="button" class="card set-card ${set.id === state.selectedSetId ? 'selected' : ''}">
          <div>
            <div class="title">${escapeHtml(set.title)}</div>
            <div class="meta">${data.questions.length} câu</div>
          </div>
        </button>
      `);
      card.addEventListener('click', () => {
        state.selectedSetId = set.id;
        render();
      });
      setsWrap.appendChild(card);
    });
    wrap.appendChild(setsWrap);

    const wrongCount = wrongNums(state.selectedSetId).length;
    const modes = [
      { id: 'all', title: 'Làm toàn bộ (theo thứ tự)', meta: 'Đi từ câu 1 đến câu cuối' },
      { id: 'shuffle', title: 'Làm toàn bộ (trộn ngẫu nhiên)', meta: 'Thứ tự câu hỏi được xáo trộn' },
      { id: 'wrong', title: 'Chỉ ôn câu từng làm sai', meta: wrongCount > 0 ? `${wrongCount} câu` : 'Chưa có câu sai nào được ghi nhận' },
    ];

    const modeWrap = el('<div class="mode-grid"></div>');
    modes.forEach(m => {
      const disabled = m.id === 'wrong' && wrongCount === 0;
      const opt = el(`
        <button type="button" class="mode-option ${state.mode === m.id ? 'selected' : ''}" style="${disabled ? 'opacity:.5;pointer-events:none;' : ''}" ${disabled ? 'disabled' : ''}>
          <div class="title">${m.title}</div>
          <div class="meta">${m.meta}</div>
        </button>
      `);
      opt.addEventListener('click', () => { state.mode = m.id; render(); });
      modeWrap.appendChild(opt);
    });
    wrap.appendChild(modeWrap);

    if (state.mode === 'all') {
      const data = window.QUIZ_DATA[state.selectedSetId];
      const max = data.questions.length;
      if (state.startFrom > max) state.startFrom = 1;
      const startFromWrap = el(`
        <div class="card" style="display:flex;align-items:center;justify-content:space-between;gap:12px;">
          <div>
            <div class="title" style="font-weight:600;">Bắt đầu từ câu số</div>
            <div class="meta">Bỏ qua các câu trước nếu đã làm rồi</div>
          </div>
          <input type="number" class="start-from-input" min="1" max="${max}" value="${state.startFrom}">
        </div>
      `);
      const input = startFromWrap.querySelector('input');
      input.addEventListener('change', () => {
        let v = parseInt(input.value, 10);
        if (!v || v < 1) v = 1;
        if (v > max) v = max;
        state.startFrom = v;
        input.value = v;
      });
      wrap.appendChild(startFromWrap);
    }

    const startBtn = el('<button class="primary">Bắt đầu</button>');
    startBtn.addEventListener('click', startQuiz);
    wrap.appendChild(startBtn);

    wrap.appendChild(el('<div class="footer-note">Tiến trình được lưu trên trình duyệt này.</div>'));
    return wrap;
  }

  function startQuiz() {
    const data = window.QUIZ_DATA[state.selectedSetId];
    let questions = data.questions.slice();
    if (state.mode === 'wrong') {
      const nums = new Set(wrongNums(state.selectedSetId));
      questions = questions.filter(q => nums.has(q.num));
      questions = shuffle(questions);
    } else if (state.mode === 'shuffle') {
      questions = shuffle(questions);
    } else if (state.mode === 'all' && state.startFrom > 1) {
      questions = questions.slice(state.startFrom - 1);
    }
    if (questions.length === 0) return;
    state.session = {
      setId: state.selectedSetId,
      setTitle: data.title,
      questions,
      index: 0,
      answers: [],
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

    const pct = Math.round((s.index / s.questions.length) * 100);
    wrap.appendChild(el(`
      <div class="progress-row"><span>Câu ${s.index + 1}/${s.questions.length}</span><span>${s.answers.filter(a => a.correct).length} đúng</span></div>
    `));
    wrap.appendChild(el(`<div class="progress-bar"><div style="width:${pct}%"></div></div>`));

    const card = el('<div class="card"></div>');
    if (q.correct_source === 'inferred') {
      card.appendChild(el('<div class="badge">Đáp án do AI suy luận — đề gốc không đánh dấu, nên kiểm tra lại</div>'));
    } else if (q.correct_source === 'corrected') {
      card.appendChild(el('<div class="badge">Đáp án đã được sửa lại — khác với chỗ đánh dấu đậm trong file gốc</div>'));
    }
    if (q.options_source === 'reconstructed') {
      card.appendChild(el('<div class="badge badge-warn">Một số phương án nhiễu do AI tự dựng lại — tài liệu gốc không liệt kê đủ 4 đáp án</div>'));
    }
    card.appendChild(el(`<div class="stem">${escapeHtml(String(q.num) + '. ' + q.stem)}</div>`));

    const optsWrap = el('<div class="options"></div>');
    let locked = false;
    const skipBtn = el('<button type="button" class="secondary">Bỏ qua câu này →</button>');
    skipBtn.addEventListener('click', () => {
      if (locked) return;
      if (s.index + 1 < s.questions.length) {
        s.index += 1;
        render();
      } else {
        state.screen = 'result';
        render();
      }
    });
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
        skipBtn.style.display = 'none';
        const isCorrect = opt.label === q.correct;
        recordAnswer(s.setId, q.num, isCorrect);
        s.answers.push({ num: q.num, chosen: opt.label, correct: isCorrect });

        Array.from(optsWrap.children).forEach(child => child.classList.add('locked'));
        if (isCorrect) {
          optEl.classList.add('correct');
        } else {
          optEl.classList.add('wrong');
          const correctEl = Array.from(optsWrap.children).find((_, i) => q.options[i].label === q.correct);
          if (correctEl) correctEl.classList.add('correct');
        }

        if (q.explanation) {
          const label = isCorrect ? 'Vì sao đúng' : 'Giải thích';
          card.appendChild(el(`
            <div class="explain-box">
              <div class="explain-title">${label}</div>
              <div class="explain-text">${escapeHtml(q.explanation)}</div>
            </div>
          `));
        }

        const nextBtn = el(`<button class="primary">${s.index + 1 < s.questions.length ? 'Câu tiếp →' : 'Xem kết quả'}</button>`);
        nextBtn.addEventListener('click', () => {
          if (s.index + 1 < s.questions.length) {
            s.index += 1;
            render();
          } else {
            state.screen = 'result';
            render();
          }
        });
        card.appendChild(nextBtn);
      });
      optsWrap.appendChild(optEl);
    });
    card.appendChild(optsWrap);
    card.appendChild(skipBtn);

    wrap.appendChild(card);
    return wrap;
  }

  function renderResult() {
    const s = state.session;
    const total = s.answers.length;
    const correctCount = s.answers.filter(a => a.correct).length;
    const pct = total ? Math.round((correctCount / total) * 100) : 0;

    const wrap = el('<div></div>');
    wrap.appendChild(el('<h1>Kết quả</h1>'));
    const card = el('<div class="card"></div>');
    card.appendChild(el(`<div class="score-big">${correctCount}/${total}</div>`));
    card.appendChild(el(`<div class="score-sub">${pct}% đúng</div>`));
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
    homeBtn.addEventListener('click', () => { state.screen = 'home'; render(); });
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
            <div class="q-stem">${escapeHtml(q.stem)}</div>
            <div class="ans-line wrong">Bạn chọn: ${CIRCLE[chosenOpt.label]} ${escapeHtml(chosenOpt.text)}</div>
            <div class="ans-line correct">Đáp án đúng: ${CIRCLE[correctOpt.label]} ${escapeHtml(correctOpt.text)}</div>
          </div>
        `);
        if (q.explanation) {
          item.appendChild(el(`
            <div class="explain-box">
              <div class="explain-title">Giải thích</div>
              <div class="explain-text">${escapeHtml(q.explanation)}</div>
            </div>
          `));
        }
        wrap.appendChild(item);
      });
    }

    return wrap;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  render();
})();
