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


// dz
function isAllHabitsCompletedYesterday() {
    if (habits.length === 0) return false;

    const yesterday = new Date()
    yesterday.setDate(yesterday.getDate() - 1)
    const yesterdayStr = yesterday.toDateString()

    for (const habit of habits) {
        const yesterdayRecord = habit.history.find(h => h.date == yesterdayStr)
        if (!yesterdayRecord || yesterdayRecord.completed < habit.goal) {
            return false
        }
    }

    return true
}

// saveData
function saveData() {
    localStorage.setItem('habits', JSON.stringify(habits));
    localStorage.setItem('currentStreak', currentStreak);
    localStorage.setItem('lastCheckDate', lastCheckDate);
}

function createHabitElement(habit, index) {
    const today = new Date().toDateString()
    const todayRecord = habit.history.find(h => h.date === today) || { completed: 0 }
    
    const habitElement = document.createElement('div')
    habitElement.className = 'habit-item'
    habitElement.innerHTML = `
        <div class="habit-header">
            <h3>${habit.name}</h3>
            <button class="delete-habit" data-index="${index}">×</button>
        </div>
        <div class="habit-progress">
            <span class="habit-count">${todayRecord.completed}/${habit.goal}</span>
            <div class="progress-bar">
                <div class="progress" style="width: ${Math.min(100, (todayRecord.completed / habit.goal) * 100)}%"></div>
            </div>
        </div>
        <div class="habit-actions">
            <button class="decrease-btn" data-index="${index}">-</button>
            <button class="increase-btn" data-index="${index}">+</button>
        </div>
    `

    return habitElement

}

function renderHabits() {
    habitsList.innerHTML = ''

    if (habits.length === 0) {
        habitsList.innerHTML = '<p class="no-habits">Додайте свою першу звичку!</p>'
        return
    }


    habits.forEach((habit, index) => {
        const habitElement = createHabitElement(habit, index)
        habitsList.appendChild(habitElement)
    })

    document.querySelectorAll('.increase-btn').forEach((btn) => {
        btn.addEventListener('click', increaseHabitCount)
    })

}

function addHabit() {}

function deleteHabit() {}

function increaseHabitCount(e) {
    const index = e.target.dataset.index
    const today = new Date().toDateString()
    const todayRecord = habits[index].history.find(h => h.date === today)

    if (todayRecord && todayRecord.completed < habits[index].goal) {
        todayRecord.completed++
        saveDate()
        renderHabits()
        updateStatistics()

        if (todayRecord.completed === habits[index].goal) {
            anime({
                targets: e.target.closest('.habit-item'),
                backgroundColor: ['#f8f9fa', '#e6fffa', '#f8f9fa'],
                borderLeftColor: ['#3498db', '#2ecc71', '#3498db'],
                duration: 1500,
                easing: 'easeOutExpo'
            });
        }

    }
}

function decreaseHabitCount() {}

function clearAllData() {}

function confirmDelete() {}

function cancelDelete() {}

function exportData() {}

function init() {}

