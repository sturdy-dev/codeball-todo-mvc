<script lang="ts">
    let description = "";

    import {tasks} from "./store.ts";

    const create = async () => {
        return fetch('https://codeball-mvc.fly.dev/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'description': description,
            })
        }).then(res => res.json())
            .then((res) => {
                tasks.add({
                    id: res.id,
                    description: description,
                    done: 0
                })
                description = "";
            });
    }

    const onKeyDown = (e: KeyboardEvent) => {
        if (e.key === 'Enter') {
            create();
        }
    }
</script>

<div class="flex items-center space-x-4 p-4">

    <input class="py-1 px-2 w-full" type="text" bind:value={description} placeholder="Add new task"
           on:keydown={onKeyDown}>
</div>
