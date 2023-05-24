import{createStore}from'vuex'

export default createStore({
  state: {
  },
  getters: {
  },
  mutations: {
    login (state) {
      state.isLogin = true
    },
    logout (state) {
      state.isLogin = false
    }
  },
  actions: {
  },
  modules: {
  }
})
