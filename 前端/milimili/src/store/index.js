import { createStore } from 'vuex'

export default createStore({
  state: {
    searchinput: '',
    isLogin: ''
  },
  mutations: {
    login(state) {
      state.isLogin = true
    },
    logout(state) {
      state.isLogin = false
      console.log(state.isLogin)
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
