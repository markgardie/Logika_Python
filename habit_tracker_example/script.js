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

// Оновлення кругового індикатора прогресу
function updateProgressCircle(completionRate) {
    const offset = CIRCLE_CIRCUMFERENCE * (1 - completionRate);
    
    anime({
        targets: '.progress-circle',
        strokeDashoffset: offset,
        duration: 800,
        easing: 'easeOutQuart'
    });
}

// Оновлення статистики
function updateStatistics() {
    // Перевірка на новий день
    const today = new Date().toDateString();
    if (lastCheckDate !== today) {
        // Якщо вчора були виконані всі звички, збільшуємо серію
        if (lastCheckDate !== '' && isAllHabitsCompletedYesterday()) {
            currentStreak++;
            
            // Анімація збільшення серії
            anime({
                targets: '#streak-days',
                scale: [1, 1.2, 1],
                duration: 1000,
                easing: 'easeOutElastic(1, .5)'
            });
        } else if (lastCheckDate !== '' && !isAllHabitsCompletedYesterday()) {
            currentStreak = 0;
        }
        
        // Скидаємо лічильники для нового дня
        habits.forEach(habit => {
            habit.history.push({ date: today, completed: 0 });
            if (habit.history.length > 30) {
                habit.history.shift();
            }
        });
        
        lastCheckDate = today;
        saveData();
    }
    
    // Розрахунок загального показника виконання
    const totalGoals = habits.reduce((sum, habit) => sum + habit.goal, 0);
    const completedToday = habits.reduce((sum, habit) => {
        const todayRecord = habit.history.find(h => h.date === today);
        return sum + (todayRecord ? todayRecord.completed : 0);
    }, 0);
    
    const completionRate = totalGoals > 0 ? completedToday / totalGoals : 0;
    
    // Оновлення відображення
    streakDisplay.textContent = currentStreak;
    completionRateDisplay.textContent = `${Math.round(completionRate * 100)}%`;
    updateProgressCircle(completionRate);
}

// Перевірка чи всі звички були виконані вчора
function isAllHabitsCompletedYesterday() {
    if (habits.length === 0) return false;
    
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1);
    const yesterdayStr = yesterday.toDateString();
    
    for (const habit of habits) {
        const yesterdayRecord = habit.history.find(h => h.date === yesterdayStr);
        if (!yesterdayRecord || yesterdayRecord.completed < habit.goal) {
            return false;
        }
    }
    return true;
}

// Збереження даних
function saveData() {
    localStorage.setItem('habits', JSON.stringify(habits));
    localStorage.setItem('currentStreak', currentStreak);
    localStorage.setItem('lastCheckDate', lastCheckDate);
}

// Створення елемента звички
function createHabitElement(habit, index) {
    const today = new Date().toDateString();
    const todayRecord = habit.history.find(h => h.date === today) || { completed: 0 };
    
    const habitElement = document.createElement('div');
    habitElement.className = 'habit-item';
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
    `;
    
    return habitElement;
}

// Оновлення списку звичок
function renderHabits() {
    habitsList.innerHTML = '';
    
    if (habits.length === 0) {
        habitsList.innerHTML = '<p class="no-habits">Додайте свою першу звичку!</p>';
        return;
    }
    
    habits.forEach((habit, index) => {
        const habitElement = createHabitElement(habit, index);
        habitsList.appendChild(habitElement);
    });
    
    // Встановлення обробників подій
    document.querySelectorAll('.increase-btn').forEach(btn => {
        btn.addEventListener('click', increaseHabitCount);
    });
    
    document.querySelectorAll('.decrease-btn').forEach(btn => {
        btn.addEventListener('click', decreaseHabitCount);
    });
    
    document.querySelectorAll('.delete-habit').forEach(btn => {
        btn.addEventListener('click', deleteHabit);
    });
}

// Додавання нової звички
function addHabit() {
    const name = habitNameInput.value.trim();
    const goal = parseInt(goalCountInput.value);
    
    if (!name || goal <= 0) {
        anime({
            targets: '#add-habit-form',
            translateX: [0, -10, 10, -10, 10, 0],
            duration: 500,
            easing: 'easeInOutSine'
        });
        return;
    }
    
    const today = new Date().toDateString();
    const newHabit = {
        name,
        goal,
        history: [{ date: today, completed: 0 }]
    };
    
    habits.push(newHabit);
    saveData();
    
    // Очищення форми
    habitNameInput.value = '';
    goalCountInput.value = '1';
    
    // Анімація та рендеринг
    renderHabits();
    updateStatistics();
    
    // Анімація появи нової звички
    if (habitsList.lastChild) {
        anime({
            targets: habitsList.lastChild,
            translateY: [50, 0],
            opacity: [0, 1],
            duration: 800,
            easing: 'easeOutQuint'
        });
    }
}

// Збільшення лічильника звички
function increaseHabitCount(e) {
    const index = e.target.dataset.index;
    const today = new Date().toDateString();
    const todayRecord = habits[index].history.find(h => h.date === today);
    
    if (todayRecord && todayRecord.completed < habits[index].goal) {
        todayRecord.completed++;
        saveData();
        renderHabits();
        updateStatistics();
        
        // Анімація завершення, якщо досягнуто ціль
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

// Зменшення лічильника звички
function decreaseHabitCount(e) {
    const index = e.target.dataset.index;
    const today = new Date().toDateString();
    const todayRecord = habits[index].history.find(h => h.date === today);
    
    if (todayRecord && todayRecord.completed > 0) {
        todayRecord.completed--;
        saveData();
        renderHabits();
        updateStatistics();
    }
}

// Видалення звички
function deleteHabit(e) {
    const index = e.target.dataset.index;
    const habitElement = e.target.closest('.habit-item');
    
    anime({
        targets: habitElement,
        translateX: 150,
        opacity: 0,
        duration: 500,
        easing: 'easeOutQuint',
        complete: function() {
            habits.splice(index, 1);
            saveData();
            renderHabits();
            updateStatistics();
        }
    });
}

// Очищення всіх даних
function clearAllData() {
    confirmModal.style.display = 'flex';
}

// Підтвердження видалення
function confirmDelete() {
    habits = [];
    currentStreak = 0;
    lastCheckDate = '';
    saveData();
    renderHabits();
    updateStatistics();
    
    confirmModal.style.display = 'none';
    
    // Анімація скидання прогресу
    anime({
        targets: '.progress-circle',
        strokeDashoffset: CIRCLE_CIRCUMFERENCE,
        duration: 800,
        easing: 'easeInOutQuad'
    });
}

// Скасування видалення
function cancelDelete() {
    confirmModal.style.display = 'none';
}

// Експорт даних
function exportData() {
    const dataStr = JSON.stringify({
        habits,
        currentStreak,
        lastCheckDate
    }, null, 2);
    
    const blob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = `habits_tracker_export_${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(a);
    a.click();
    
    setTimeout(() => {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }, 0);
}

// Ініціалізація
function init() {
    renderHabits();
    updateStatistics();
    
    // Додавання обробників подій
    addHabitBtn.addEventListener('click', addHabit);
    
    habitNameInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            addHabit();
        }
    });
    
    clearAllBtn.addEventListener('click', clearAllData);
    exportDataBtn.addEventListener('click', exportData);
    confirmDeleteBtn.addEventListener('click', confirmDelete);
    cancelDeleteBtn.addEventListener('click', cancelDelete);
}

// Запуск додатку
document.addEventListener('DOMContentLoaded', init);