(function () {
  const KEY_STORAGE = 'kiip5_admin_key';
  const AUTH_STORAGE = 'kiip5_auth_v1';
  const root = document.getElementById('admin-app');

  function el(html) {
    const t = document.createElement('template');
    t.innerHTML = html.trim();
    return t.content.firstElementChild;
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  function getSavedKey() {
    try { return localStorage.getItem(KEY_STORAGE) || ''; } catch (e) { return ''; }
  }

  function saveKey(key) {
    try { localStorage.setItem(KEY_STORAGE, key); } catch (e) { /* ignore */ }
  }

  function clearKey() {
    try { localStorage.removeItem(KEY_STORAGE); } catch (e) { /* ignore */ }
  }

  function clearAdminAuth() {
    try { localStorage.removeItem(AUTH_STORAGE); } catch (e) { /* ignore */ }
  }

  function getAdminAuth() {
    try {
      const auth = JSON.parse(localStorage.getItem(AUTH_STORAGE) || 'null');
      return auth?.role === 'admin' && auth?.token ? auth : null;
    } catch (e) {
      return null;
    }
  }

  function renderLogin(errorMsg) {
    root.innerHTML = '';
    const wrap = el('<div class="login-box"></div>');
    wrap.appendChild(el('<h1 style="text-align:center;">📊 Thống kê truy cập</h1>'));
    wrap.appendChild(el('<div class="subtitle" style="text-align:center;">Nhập mật khẩu admin để xem</div>'));
    const card = el('<div class="card"></div>');
    const input = el('<input type="password" placeholder="Mật khẩu admin">');
    card.appendChild(input);
    const btn = el('<button class="primary">Xem thống kê</button>');
    card.appendChild(btn);
    card.appendChild(el(`<div class="err-msg">${errorMsg ? escapeHtml(errorMsg) : ''}</div>`));
    wrap.appendChild(card);
    root.appendChild(wrap);

    const submit = () => {
      const key = input.value.trim();
      if (!key) return;
      saveKey(key);
      loadStats();
    };
    btn.addEventListener('click', submit);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') submit(); });
    input.focus();
  }

  function dayLabel(dateStr) {
    const d = new Date(dateStr + 'T00:00:00Z');
    return `${d.getUTCDate()}/${d.getUTCMonth() + 1}`;
  }

  function renderUsersSection(users) {
    const wrap = el('<div></div>');
    wrap.appendChild(el(`<div class="section-label">Người dùng đã đăng ký (${users.length})</div>`));
    if (users.length === 0) {
      wrap.appendChild(el('<div class="card"><div class="meta">Chưa có ai đăng ký tài khoản.</div></div>'));
      return wrap;
    }
    const tableWrap = el('<div class="table-wrap"></div>');
    const table = el(`
      <table class="visits">
        <thead>
          <tr><th>Tên hiển thị</th><th>Tài khoản</th><th>Đã làm</th><th>Đúng</th><th>Hoạt động gần nhất</th></tr>
        </thead>
        <tbody></tbody>
      </table>
    `);
    const tbody = table.querySelector('tbody');
    users.forEach(u => {
      const last = u.updatedAt ? new Date(u.updatedAt).toLocaleString('vi-VN') : '—';
      const row = el(`
        <tr>
          <td>${escapeHtml(u.displayName || u.username)}</td>
          <td>${escapeHtml(u.username)}</td>
          <td>${u.seen}</td>
          <td>${u.pct}%</td>
          <td>${escapeHtml(last)}</td>
        </tr>
      `);
      tbody.appendChild(row);
    });
    tableWrap.appendChild(table);
    wrap.appendChild(tableWrap);
    return wrap;
  }

  function renderDashboard(data, usersData) {
    root.innerHTML = '';
    const topBar = el('<div class="top-bar"></div>');
    topBar.appendChild(el('<h1 style="margin:0;">📊 Thống kê truy cập</h1>'));
    const logoutBtn = el('<button class="link-btn">Đăng xuất</button>');
    logoutBtn.addEventListener('click', () => { clearKey(); clearAdminAuth(); renderLogin(); });
    topBar.appendChild(logoutBtn);
    root.appendChild(topBar);

    const statGrid = el('<div class="stat-grid"></div>');
    statGrid.appendChild(el(`<div class="card stat-card"><b>${data.total}</b><span>Tổng IP truy cập</span></div>`));
    statGrid.appendChild(el(`<div class="card stat-card"><b>${data.totalVisits || 0}</b><span>Lượt ghi nhận</span></div>`));
    statGrid.appendChild(el(`<div class="card stat-card"><b>${data.today}</b><span>IP hôm nay</span></div>`));
    root.appendChild(statGrid);

    if (usersData && usersData.users) {
      root.appendChild(renderUsersSection(usersData.users));
    }

    const days = data.perDay.slice(0, 14).slice().reverse();
    if (days.length > 0) {
      const maxCount = Math.max(...days.map(d => d.count), 1);
      const chartCard = el('<div class="card"></div>');
      chartCard.appendChild(el('<div class="section-label" style="margin-top:0;">14 ngày gần nhất</div>'));
      const bars = el('<div class="day-bars"></div>');
      const labels = el('<div class="day-labels"></div>');
      days.forEach(d => {
        const h = Math.max(3, Math.round((d.count / maxCount) * 90));
        const bar = el(`<div class="day-bar" style="height:${h}px" title="${escapeHtml(d.date)}: ${d.count} lượt"></div>`);
        bars.appendChild(bar);
        labels.appendChild(el(`<span>${dayLabel(d.date)}</span>`));
      });
      chartCard.appendChild(bars);
      chartCard.appendChild(labels);
      root.appendChild(chartCard);
    }

    root.appendChild(el('<div class="section-label">Lượt truy cập gần đây</div>'));
    const tableWrap = el('<div class="table-wrap"></div>');
    const table = el(`
      <table class="visits">
        <thead>
          <tr><th>Thời gian</th><th>IP</th><th>Vị trí</th><th>Trang</th><th>Trình duyệt</th></tr>
        </thead>
        <tbody></tbody>
      </table>
    `);
    const tbody = table.querySelector('tbody');
    const appendVisits = visits => {
      [...visits]
        .sort((a, b) => Date.parse(b.ts || 0) - Date.parse(a.ts || 0))
        .forEach(v => {
          const time = v.ts ? new Date(v.ts).toLocaleString('vi-VN') : '';
          const loc = [v.city, v.country].filter(Boolean).join(', ') || '—';
          const row = el(`
            <tr>
              <td>${escapeHtml(time)}</td>
              <td>${escapeHtml(v.ip || '')}</td>
              <td>${escapeHtml(loc)}</td>
              <td>${escapeHtml(v.page || '')}</td>
              <td title="${escapeHtml(v.userAgent || '')}">${escapeHtml((v.userAgent || '').slice(0, 40))}</td>
            </tr>
          `);
          tbody.appendChild(row);
        });
    };
    appendVisits(data.recent || []);
    tableWrap.appendChild(table);
    root.appendChild(tableWrap);

    if (data.nextCursor) {
      const moreBtn = el('<button class="secondary" style="display:block;margin:12px auto;">더보기</button>');
      let nextCursor = data.nextCursor;
      moreBtn.addEventListener('click', async () => {
        moreBtn.disabled = true;
        moreBtn.textContent = 'Đang tải...';
        try {
          const key = getSavedKey();
          const adminAuth = getAdminAuth();
          const headers = adminAuth ? { Authorization: `Bearer ${adminAuth.token}` } : {};
          const params = new URLSearchParams({ cursor: nextCursor });
          if (key) params.set('key', key);
          const res = await fetch(`/.netlify/functions/admin-stats?${params}`, { headers });
          if (res.status === 401) {
            clearKey();
            clearAdminAuth();
            renderLogin('Phiên quản trị không hợp lệ hoặc đã hết hạn.');
            return;
          }
          if (!res.ok) throw new Error('Không thể tải thêm dữ liệu.');
          const page = await res.json();
          appendVisits(page.recent || []);
          nextCursor = page.nextCursor;
          if (!nextCursor) {
            moreBtn.remove();
            return;
          }
          moreBtn.disabled = false;
          moreBtn.textContent = '더보기';
        } catch (error) {
          moreBtn.disabled = false;
          moreBtn.textContent = 'Thử lại';
        }
      });
      root.appendChild(moreBtn);
    }

    const refreshBtn = el('<button class="secondary">Làm mới</button>');
    refreshBtn.addEventListener('click', loadStats);
    root.appendChild(refreshBtn);
  }

  async function loadStats() {
    const key = getSavedKey();
    const adminAuth = getAdminAuth();
    if (!key && !adminAuth) { renderLogin(); return; }
    root.innerHTML = '<div class="subtitle" style="text-align:center;margin-top:60px;">Đang tải...</div>';
    try {
      const headers = adminAuth ? { Authorization: `Bearer ${adminAuth.token}` } : {};
      const query = key ? `?key=${encodeURIComponent(key)}` : '';
      const [statsRes, usersRes] = await Promise.all([
        fetch(`/.netlify/functions/admin-stats${query}`, { headers }),
        fetch(`/.netlify/functions/admin-users${query}`, { headers }),
      ]);
      if (statsRes.status === 401) { clearKey(); clearAdminAuth(); renderLogin('Phiên quản trị không hợp lệ hoặc đã hết hạn.'); return; }
      if (!statsRes.ok) {
        const err = await statsRes.json().catch(() => ({}));
        renderLogin(err.error || 'Không thể tải dữ liệu.');
        return;
      }
      const data = await statsRes.json();
      const usersData = usersRes.ok ? await usersRes.json() : { users: [] };
      renderDashboard(data, usersData);
    } catch (e) {
      renderLogin('Không thể kết nối máy chủ.');
    }
  }

  loadStats();
})();
