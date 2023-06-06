import { createStore } from 'vuex'

export default createStore({
  state: {
    searchinput: ''
  },
  getters: {
  },
  mutations: {
    login(state) {
      state.isLogin = true
    },
    logout(state) {
      state.isLogin = false
    },
    setSearchInput(state, value) {
      state.searchinput = value;
    },
  },
  actions: {
    updateSearchInput({ commit }, value) {
      commit('setSearchInput', value);
    },
  },
  modules: {
  }
})
