import "ant-design-vue/dist/reset.css";
import "./style.css";
import "../node_modules/flowbite-vue/dist/index.css";

import { createApp } from "vue";
import store from "./store";
import Antd from "ant-design-vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);
app.use(Antd);
app.use(store);

app.mount("#app");
