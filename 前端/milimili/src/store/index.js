import { createStore } from 'vuex'

export default createStore({
  state:{
    id:'1',
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
    setid(state,value){
      state.id=value;
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
