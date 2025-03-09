// Елементи інтерфейсу
const habitsList = document.getElementById('habits-list');
const addHabitBtn = document.getElementById('add-habit');
const habitNameInput = document.getElementById('habit-name');
const goalCountInput = document.getElementById('goal-count');
const streakDisplay = document.getElementById('streak-days');
const completionRateDisplay = document.getElementById('completion-rate');
const progressCircle = document.querySelector('.progress-circle');
const clearAllBtn = document.getElementById('clear-all');
const exportDataBtn = document.getElementById('export-data');
const confirmModal = document.getElementById('confirm-modal');
const confirmDeleteBtn = document.getElementById('confirm-delete');
const cancelDeleteBtn = document.getElementById('cancel-delete');

// Константи для анімації
const CIRCLE_RADIUS = 45;
const CIRCLE_CIRCUMFERENCE = 2 * Math.PI * CIRCLE_RADIUS;
progressCircle.style.strokeDasharray = `${CIRCLE_CIRCUMFERENCE} ${CIRCLE_CIRCUMFERENCE}`;

// Дані та стан
let habits = JSON.parse(localStorage.getItem('habits')) || [];
let currentStreak = parseInt(localStorage.getItem('currentStreak')) || 0;
let lastCheckDate = localStorage.getItem('lastCheckDate') || '';

function updateProgressCircle(completionRate) {
    const offset = CIRCLE_CIRCUMFERENCE * (1 - completionRate)

    anime({
        targets: '.progress-circle',
        strokeDashoffset: offset,
        duration: 800,
        easing: 'easeOutQuad'
    })
}

function isAllHabitsCompletedYesterday() {
    if (habits.length === 0) return false;

    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayStr = yesterday.toDateString()

    for (const habit of habits) {
        const yesterdayRecord = habit.history.find(h => h.date == yesterdayStr)
    }
}
