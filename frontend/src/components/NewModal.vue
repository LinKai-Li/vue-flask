<script setup>
import { defineProps, defineEmits, reactive } from "vue";
import { useStore } from "vuex";
import { useToast } from "vue-toastification";
import { options } from "@/constant/options";
import {
  FwbButton,
  FwbModal,
  FwbInput,
  FwbCheckbox,
  FwbSelect,
} from "flowbite-vue";
defineProps({
  modelValue: Boolean,
});

const toast = useToast();

const emit = defineEmits(["update:modelValue"]);

const store = useStore();
const addGame = (addGameForm) => {
  store.dispatch("addGame", addGameForm);
  toast.success("Game added");
};

const addGameForm = reactive({
  title: "",
  genre: "",
  played: false,
});

const initForm = () => {
  addGameForm.title = "";
  addGameForm.genre = "";
  addGameForm.played = false;
};

const handleOk = () => {
  emit("update:modelValue", false);
  addGame(addGameForm);
  initForm();
};

const closeModal = () => {
  emit("update:modelValue", false);
  initForm();
};
</script>

<template>
  <fwb-modal v-if="modelValue" @close="closeModal">
    <template #header>
      <div class="flex items-center text-lg">Add a new game</div>
    </template>
    <template #body>
      <div class="flex flex-col gap-4">
        <fwb-input
          v-model="addGameForm.title"
          placeholder="Enter Title"
          label="Title"
        />
        <fwb-select
          v-model="addGameForm.genre"
          :options="options"
          label="Genre"
        />
        <fwb-checkbox v-model="addGameForm.played" label="Played?" />
      </div>
    </template>
    <template #footer>
      <div class="flex justify-end gap-2">
        <fwb-button @click="closeModal" color="alternative">
          Cancel
        </fwb-button>
        <fwb-button @click="handleOk"> Submit </fwb-button>
      </div>
    </template>
  </fwb-modal>
</template>
