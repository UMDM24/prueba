const API_BASE = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {
    loadCategories();
    loadAreas();
    
});

/* =====================
   LOAD DROPDOWNS
===================== */
async function loadCategories() {
    const res = await fetch(`${API_BASE}/lists/categories/all`);
    const data = await res.json();
    const select = document.getElementById("categorySelect");

    data.meals.forEach(c => {
        const option = document.createElement("option");
        option.value = c.strCategory;
        option.textContent = c.strCategory;
        select.appendChild(option);
    });
}

async function loadAreas() {
    const res = await fetch(`${API_BASE}/lists/areas`);
    const data = await res.json();
    const select = document.getElementById("areaSelect");

    data.meals.forEach(a => {
        const option = document.createElement("option");
        option.value = a.strArea;
        option.textContent = a.strArea;
        select.appendChild(option);
    });
}



/* =====================
   SEARCH FUNCTIONS
===================== */
async function searchByName() {
    const name = document.getElementById("mealName").value;
    if (!name) return;

    const res = await fetch(`${API_BASE}/meals/search?name=${name}`);
    const data = await res.json();
    renderMeals(data.meals);
}

async function searchByLetter() {
    const letter = document.getElementById("mealLetter").value;
    if (!letter) return;

    const res = await fetch(`${API_BASE}/meals/letter/${letter}`);
    const data = await res.json();
    renderMeals(data.meals);
}

async function searchByCategory() {
    const category = document.getElementById("categorySelect").value;
    if (!category) return;

    const res = await fetch(`${API_BASE}/filters/category/${category}`);
    const data = await res.json();
    renderFilteredMeals(data.meals);
}

async function searchByArea() {
    const area = document.getElementById("areaSelect").value;
    if (!area) return;

    const res = await fetch(`${API_BASE}/filters/area/${area}`);
    const data = await res.json();
    renderFilteredMeals(data.meals);
}



/* =====================
   RENDER
===================== */
function renderMeals(meals) {
    const container = document.getElementById("results");
    container.innerHTML = "";

    if (!meals || meals.length === 0) {
        container.innerHTML = "No hay resultados";
        return;
    }

    meals.forEach(meal => {
        container.innerHTML += `
            <div class="card">
                <img src="${meal.images.medium}">
                <h3>${meal.name}</h3>
                <p><b>${meal.category}</b> - ${meal.area}</p>
            </div>
        `;
    });
}

function renderFilteredMeals(meals) {
    const container = document.getElementById("results");
    container.innerHTML = "";

    if (!meals || meals.length === 0) {
        container.innerHTML = "No hay resultados";
        return;
    }

    meals.forEach(meal => {
        container.innerHTML += `
            <div class="card">
                <img src="${meal.strMealThumb}">
                <h3>${meal.strMeal}</h3>
            </div>
        `;
    });
}
