import { writable } from 'svelte/store';
import type { Task } from './types';

function createTasks() {
	const { subscribe, set, update } = writable<Array<Task>>();

	return {
		subscribe,
		set,
		add: (t: Task) => update((tasks) => [...tasks, t]),
		update: (t: Task) => update((tasks) => tasks.map((task) => (task.id === t.id ? t : task)))
	};
}

export const tasks = createTasks();
