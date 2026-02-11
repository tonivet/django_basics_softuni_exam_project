
  const select = document.getElementById('statusSelect');
  const storageKey = 'statusSelectValue';

  // Restore after reload
  const saved = localStorage.getItem(storageKey);
  if (saved) {
    select.value = saved;
  }

  // Save on change
  select.addEventListener('change', function () {
    localStorage.setItem(storageKey, this.value);
  });

