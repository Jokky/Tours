import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    tours: []
  },
  getters: {
    getTours: state => state.tours
  },
  mutations: {
    ADD_TOURS(state, tours) {
      state.tours = tours
    }
  },
})
