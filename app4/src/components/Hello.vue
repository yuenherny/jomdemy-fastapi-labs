<template>
    <div>
        <h1>Hello World</h1>
        <button @click="doClick">Click me</button>
        <button @click="doFetch">Fetch event</button>
        <li v-for="event in events">{{ event.title }}</li>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                events: []
            }
        },
        methods: {
            doClick() {
                alert("You clicked me");
            },
            doFetch() {
                fetch("http://localhost:8000/event/")
                .then(data => data.json())
                .then(json => {
                    console.log(json);
                    this.events = json;
                })
            }
        }
    }
</script>

<style>
    h1 {
        color: red;
    }
</style>