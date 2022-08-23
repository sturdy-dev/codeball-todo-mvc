<script lang="ts">
    import type {Task} from "./types";
    import {tasks} from "./store.ts";

    export let task: Task;

    const update = async () => {
        return fetch('https://codeball-mvc.fly.dev/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'id': task.id as string,
                'description': task.description,
                'done': task.done as string,
            })
        }).then(() => {
            tasks.update(task)
        });
    }

    const markDone = async () => {
        task.done = 1
        return update()
    }

    const markTodo = async () => {
        task.done = 0
        return update()
    }
</script>

<div class="flex items-center space-x-4 p-4"
     class:line-through={task.done}
     class:bg-green-200={task.done}
     class:bg-gray-100={!task.done}
>
    {#if !task.done}
        <button on:click={markDone}>⬜️</button>
    {:else}
        <button on:click={markTodo}>✅️</button>
    {/if}

    <div>
        {task.description}
    </div>
</div>
