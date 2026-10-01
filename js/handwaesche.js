(() => {
  const form = document.getElementById('wash-booking-form');
  if (!form) return;

  const dateInput = document.getElementById('wash-date');
  const calendarDays = document.getElementById('wash-calendar-days');
  const monthLabel = document.getElementById('wash-month-label');
  const prevMonth = document.getElementById('wash-prev-month');
  const nextMonth = document.getElementById('wash-next-month');
  const slots = document.getElementById('wash-slots');
  const steps = [...form.querySelectorAll('.wash-step')];
  const progress = [...form.querySelectorAll('.wash-progress li')];
  const status = document.getElementById('wash-status');
  const submit = document.getElementById('wash-submit');
  const vehicleInput = document.getElementById('wash-vehicle');
  const yearInput = document.getElementById('wash-year');
  const nameInput = document.getElementById('wash-name');
  const emailInput = document.getElementById('wash-email');
  const phoneInput = document.getElementById('wash-phone');
  const berlinToday = () => {
    const parts = new Intl.DateTimeFormat('en-CA', {
      timeZone: 'Europe/Berlin', year: 'numeric', month: '2-digit', day: '2-digit'
    }).formatToParts(new Date());
    const get = (type) => parts.find((part) => part.type === type).value;
    return `${get('year')}-${get('month')}-${get('day')}`;
  };
  const parseDate = (value) => {
    const [year, month, day] = value.split('-').map(Number);
    return new Date(Date.UTC(year, month - 1, day));
  };
  const toISO = (date) => date.toISOString().slice(0, 10);
  const addDay = (date) => new Date(date.getTime() + 86400000);
  const isWorkday = (date) => date.getUTCDay() >= 1 && date.getUTCDay() <= 5;
  const monthIndex = (date) => date.getUTCFullYear() * 12 + date.getUTCMonth();
  const formatDate = (value) => new Intl.DateTimeFormat('de-DE', {
    timeZone: 'UTC', weekday: 'long', day: 'numeric', month: 'long', year: 'numeric'
  }).format(parseDate(value));
  let currentStep = 0;

  // Ein vollständiger Montag-bis-Freitag-Tag liegt zwischen Anfrage und Termin.
  function earliestDate() {
    let date = parseDate(berlinToday());
    do { date = addDay(date); } while (!isWorkday(date));
    do { date = addDay(date); } while (!isWorkday(date));
    return toISO(date);
  }

  const today = parseDate(berlinToday());
  const firstMonth = new Date(Date.UTC(today.getUTCFullYear(), today.getUTCMonth(), 1));
  let visibleMonth = new Date(firstMonth);

  function showStatus(state, message) {
    status.dataset.state = state;
    status.textContent = message;
  }

  function renderCalendar() {
    const year = visibleMonth.getUTCFullYear();
    const month = visibleMonth.getUTCMonth();
    monthLabel.textContent = new Intl.DateTimeFormat('de-DE', {
      timeZone: 'UTC', month: 'long', year: 'numeric'
    }).format(visibleMonth);
    prevMonth.disabled = monthIndex(visibleMonth) <= monthIndex(firstMonth);
    nextMonth.disabled = monthIndex(visibleMonth) >= monthIndex(firstMonth) + 11;
    calendarDays.replaceChildren();
    const offset = (visibleMonth.getUTCDay() + 6) % 7;
    for (let index = 0; index < offset; index += 1) {
      calendarDays.append(document.createElement('span'));
    }
    const daysInMonth = new Date(Date.UTC(year, month + 1, 0)).getUTCDate();
    for (let day = 1; day <= daysInMonth; day += 1) {
      const date = new Date(Date.UTC(year, month, day));
      const iso = toISO(date);
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = String(day);
      button.setAttribute('aria-label', formatDate(iso));
      button.setAttribute('aria-pressed', iso === dateInput.value ? 'true' : 'false');
      button.disabled = iso < earliestDate() || !isWorkday(date);
      button.addEventListener('click', () => {
        dateInput.value = iso;
        showStatus('', '');
        renderCalendar();
        renderSlots();
      });
      calendarDays.append(button);
    }
  }

  function renderSlots() {
    const chosen = slots.querySelector('input:checked')?.value;
    slots.replaceChildren();
    for (let hour = 9; hour <= 15; hour += 1) {
      const label = document.createElement('label');
      const input = document.createElement('input');
      const text = document.createElement('span');
      input.type = 'radio';
      input.name = 'time';
      input.value = `${String(hour).padStart(2, '0')}:00`;
      input.required = true;
      input.checked = input.value === chosen;
      text.textContent = `${hour}:00`;
      label.append(input, text);
      slots.append(label);
    }
  }

  function setStep(index) {
    currentStep = index;
    steps.forEach((step, i) => { step.hidden = i !== index; });
    progress.forEach((item, i) => {
      item.classList.toggle('is-active', i === index);
      item.classList.toggle('is-done', i < index);
      if (i === index) item.setAttribute('aria-current', 'step');
      else item.removeAttribute('aria-current');
    });
    if (index >= 1 && dateInput.value) {
      document.getElementById('wash-selected-date').textContent = `Wunschtag: ${formatDate(dateInput.value)}`;
    }
    if (index === 2) {
      const time = form.querySelector('input[name="time"]:checked')?.value || '';
      document.getElementById('wash-summary').textContent = `${formatDate(dateInput.value)}, ${time} Uhr · ${vehicleInput.value.trim()} · Baujahr ${yearInput.value.trim()}`;
    }
    showStatus('', '');
  }

  function validateStep(index) {
    if (index === 0) {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(dateInput.value) ||
          dateInput.value < earliestDate() || !isWorkday(parseDate(dateInput.value))) {
        showStatus('error', 'Bitte wähle einen verfügbaren Werktag im Kalender.');
        return false;
      }
    }
    if (index === 1) {
      const time = form.querySelector('input[name="time"]:checked')?.value || '';
      if (!/^(09|10|11|12|13|14|15):00$/.test(time)) {
        showStatus('error', 'Bitte wähle eine Startzeit.');
        return false;
      }
      for (const input of [vehicleInput, yearInput]) {
        const valid = input.value.trim() && input.checkValidity();
        input.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid) {
          showStatus('error', 'Bitte Fahrzeug und Baujahr vollständig eingeben.');
          input.focus();
          return false;
        }
      }
      const year = Number(yearInput.value);
      if (year < 1900 || year > parseDate(berlinToday()).getUTCFullYear() + 1) {
        showStatus('error', 'Bitte ein gültiges Baujahr eingeben.');
        yearInput.focus();
        return false;
      }
    }
    if (index === 2) {
      for (const input of [nameInput, emailInput, phoneInput]) {
        const valid = input.value.trim() && input.checkValidity();
        input.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid) {
          showStatus('error', 'Bitte Name, gültige E-Mail-Adresse und Telefonnummer eingeben.');
          input.focus();
          return false;
        }
      }
    }
    return true;
  }

  prevMonth.addEventListener('click', () => {
    visibleMonth = new Date(Date.UTC(visibleMonth.getUTCFullYear(), visibleMonth.getUTCMonth() - 1, 1));
    renderCalendar();
  });
  nextMonth.addEventListener('click', () => {
    visibleMonth = new Date(Date.UTC(visibleMonth.getUTCFullYear(), visibleMonth.getUTCMonth() + 1, 1));
    renderCalendar();
  });
  form.querySelectorAll('[data-next]').forEach((button) => button.addEventListener('click', () => {
    if (validateStep(currentStep)) setStep(currentStep + 1);
  }));
  form.querySelectorAll('[data-back]').forEach((button) => button.addEventListener('click', () => setStep(currentStep - 1)));
  renderCalendar();
  renderSlots();
  setStep(0);

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!validateStep(0)) { setStep(0); showStatus('error', 'Bitte wähle erneut einen gültigen Wunschtag.'); return; }
    if (!validateStep(1)) { setStep(1); showStatus('error', 'Bitte prüfe Startzeit und Fahrzeug.'); return; }
    if (!validateStep(2)) return;
    const data = new FormData(form);
    const date = String(data.get('date'));
    const time = String(data.get('time'));
    const name = String(data.get('name')).trim();
    const email = String(data.get('email')).trim();
    const phone = String(data.get('phone')).trim();
    const vehicle = String(data.get('vehicle')).trim();
    const year = String(data.get('year')).trim();
    submit.disabled = true;
    showStatus('sending', 'Anfrage wird gesendet …');
    try {
      const response = await fetch('/api/send-lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          formName: 'Exklusive Handwäsche Terminanfrage',
          website: String(data.get('website') || ''),
          name, email, phone, vehicle, year, date, time,
          message: `Terminanfrage für exklusive Auto-Handwäsche am ${date} um ${time} Uhr. Fahrzeug: ${vehicle}, Baujahr: ${year}. Aktionspreis: 50 €.`
        })
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || 'Versand fehlgeschlagen.');
      form.reset();
      renderCalendar();
      renderSlots();
      setStep(0);
      showStatus('success', 'Danke! Deine Terminanfrage ist eingegangen. Wir melden uns zur Bestätigung.');
    } catch (error) {
      showStatus('error', error.message || 'Versand fehlgeschlagen. Bitte ruf uns an.');
    } finally {
      submit.disabled = false;
    }
  });
})();
