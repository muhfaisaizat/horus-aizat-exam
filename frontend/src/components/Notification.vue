<template>
  <transition name="slide-down">
    <div v-if="open" class="fixed top-1.5 left-1/2 transform -translate-x-1/2 z-50">
      <div :class="[
        'relative px-6 py-4 shadow-lg text-white flex flex-col items-center gap-2 min-w-[320px] text-center rounded-lg',
        type === 'success'
          ? 'bg-green-500'
          : type === 'error'
            ? 'bg-red-500'
            : type === 'info'
              ? 'bg-blue-500'
              : 'bg-gray-600'
      ]">

        <button @click="$emit('close')" class="absolute top-2 right-3 text-white hover:text-gray-200 font-bold text-xl">
          ✕
        </button>

        <h3 class="font-bold text-lg">{{ title }}</h3>
        <p class="text-sm">{{ message }}</p>

        <button v-if="buttonText" @click="$emit('buttonClick')"
          class="mt-2 bg-white text-black px-4 py-1 rounded hover:bg-gray-200 transition-colors">
          {{ buttonText }}
        </button>

      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: "Notification",
  props: {
    open: Boolean,
    title: String,
    message: String,
    type: {
      type: String,
      default: "success",
    },
    buttonText: {
      type: String,
      default: "",
    },
  },
  emits: ["close", "buttonClick"],
};
</script>

<style scoped>
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
}

.slide-down-enter-from {
  opacity: 0;
  transform: translateY(-30px);
}

.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-30px);
}
</style>
