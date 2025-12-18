document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');
  const registerForm = document.getElementById('registerForm');
  const searchForm = document.getElementById('searchForm');

  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Login functionality coming soon!');
    });
  }

  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Register functionality coming soon!');
    });
  }

  if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const location = document.getElementById('location').value;
      document.getElementById('results').innerHTML = `<p>Showing mechanics near <b>${location}</b> (demo)</p>`;
    });
  }
});
