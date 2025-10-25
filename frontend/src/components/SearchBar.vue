<template>
    <div class="w-full max-w-md mx-auto">
        <div class="relative">
            <input type="text" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)"
                placeholder="Search..."
                class="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500" />
            <svg class="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" fill="none"
                stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                    d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1110.5 3a7.5 7.5 0 016.15 13.65z"></path>
            </svg>
        </div>
    </div>
</template>

<script>
export default {
    name: "SearchBar",
    props: {
        modelValue: {
            type: String,
            default: "",
        },
    },
};
</script>

<style scoped>
/* Opsional */
</style>
