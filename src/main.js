import Vue from "vue";
import Vuetify from "vuetify";

import App from "./App.vue";
import router from "./router";
import store from "./store";
import "vuetify/dist/vuetify.min.css";

Vue.config.productionTip = false;
Vue.use(Vuetify, {
  theme: {
    primary: "#B2DDF7",
    secondary: "#003249",
    accent: "#FFE8E1"
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
