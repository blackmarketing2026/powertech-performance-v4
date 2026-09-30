(() => {
  const form = document.getElementById('wash-booking-form');
  if (!form) return;

  const dateInput = document.getElementById('wash-date');
  const slots = document.getElementById('wash-slots');
  const status = document.getElementById('wash-status');
  const submit = document.getElementById('wash-submit');
  const berlinToday = () => {
    const parts = new Intl.DateTimeFormat('de-DE', {
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
  const weekday = (date) => date.getUTCDay();
  const addDay = (date) => new Date(date.getTime() + 86400000);
  const isWorkday = (date) => weekday(date) >= 1 && weekday(date) <= 5;

  // Ein vollständiger Montag-bis-Freitag-Tag liegt zwischen Anfrage und Termin.
  function earliestDate() {
    let date = parseDate(berlinToday());
    let gap = 0;
    while (gap < 1) {
      date = addDay(date);
      if (isWorkday(date)) gap += 1;
    }
    do { date = addDay(date); } while (!isWorkday(date));
    return toISO(date);
  }

  function showStatus(state, message) {
    status.dataset.state = state;
    status.textContent = message;
  }

  function renderSlots() {
    slots.replaceChildren();
    const selectedDate = dateInput.value;
    if (!selectedDate) {
      slots.textContent = 'Bitte zuerst einen Tag wählen.';
      return;
    }
    if (selectedDate < earliestDate() || !isWorkday(parseDate(selectedDate))) {
      slots.textContent = 'Bitte einen gültigen Arbeitstag mit einem freien Arbeitstag Abstand wählen.';
      return;
    }
    for (let hour = 9; hour <= 15; hour += 1) {
      const label = document.createElement('label');
      const input = document.createElement('input');
      const text = document.createElement('span');
      input.type = 'radio';
      input.name = 'time';
      input.value = `${String(hour).padStart(2, '0')}:00`;
      input.required = true;
      text.textContent = `${hour}:00`;
      label.append(input, text);
      slots.append(label);
    }
  }

  dateInput.min = earliestDate();
  dateInput.addEventListener('change', renderSlots);
  dateInput.addEventListener('input', renderSlots);
  renderSlots();

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const date = String(data.get('date') || '');
    const time = String(data.get('time') || '');
    const name = String(data.get('name') || '').trim();
    const phone = String(data.get('phone') || '').trim();
    const vehicle = String(data.get('vehicle') || '').trim();
    const year = String(data.get('year') || '').trim();
    if (!date || date < earliestDate() || !isWorkday(parseDate(date)) || !/^(09|10|11|12|13|14|15):00$/.test(time)) {
      showStatus('error', 'Bitte einen gültigen Tag und eine Startzeit auswählen.');
      return;
    }
    if (!name || !phone || !vehicle || !/^\d{4}$/.test(year) || Number(year) < 1900 || Number(year) > new Date().getFullYear() + 1) {
      showStatus('error', 'Bitte Name, Telefonnummer, Fahrzeug und Baujahr vollständig eingeben.');
      return;
    }
    submit.disabled = true;
    showStatus('sending', 'Anfrage wird gesendet …');
    try {
      const response = await fetch('/api/send-lead', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          formName: 'Intensiv-Handwäsche Terminanfrage',
          website: String(data.get('website') || ''),
          name, phone, vehicle, year, date, time,
          message: `Terminanfrage für Intensiv-Auto-Handwäsche am ${date} um ${time} Uhr. Fahrzeug: ${vehicle}, Baujahr: ${year}. Aktionspreis: 50 €.`
        })
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || 'Versand fehlgeschlagen.');
      showStatus('success', 'Danke! Deine Terminanfrage ist eingegangen. Wir melden uns zur Bestätigung.');
      form.reset();
      dateInput.min = earliestDate();
      renderSlots();
    } catch (error) {
      showStatus('error', error.message || 'Versand fehlgeschlagen. Bitte ruf uns an.');
    } finally {
      submit.disabled = false;
    }
  });
})();
