import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'

import moment from 'moment'

Vue.filter('formatDate', (value) => {
  if(value)
    return moment(String(value)).format('DD.MM')
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
