const taskInputElement = document.getElementById("task_input");
const tasksElement = document.getElementById("tasks");
const btn = document.getElementById("btn");
const normalElement = document.getElementById("normal");
const lowElement = document.getElementById("low");
const highElement = document.getElementById("high");
const form = document.querySelector("form");
let tasks = [];
const addTask = (e) => {
  e.preventDefault();
  console.log(form.input.value);
  const taskValue = taskInputElement.value.trim();
  const priority = normalElement.checked
    ? "normal"
    : lowElement.checked
      ? "low"
      : "high";
  task = {
    id: Date.now(),
    text: taskValue,
    priority: priority,
  };
  tasks.push(task);
};

form.addEventListener("submit", addTask);

btn.addEventListener("click", addTask);
