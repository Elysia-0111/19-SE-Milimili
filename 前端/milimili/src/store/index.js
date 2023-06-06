import { getToken, setToken, removeToken } from '@/request/token'
import { createStore } from 'vuex'

export default createStore({
  state: {
    id: '',
    account: '',
    name: '',
    avatar: '',
    token: getToken(),
    searchinput: ''
  },
  getters: {
  },
  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token;
    },
    SET_ACCOUNT: (state, account) => {
      state.account = account
    },
    SET_NAME: (state, name) => {
      state.name = name
    },
    SET_AVATAR: (state, avatar) => {
      state.avatar = avatar
    },
    SET_ID: (state, id) => {
      state.id = id
    },
    SET_SELECTTABLE: (state, selecttable) => {
      state.selecttable = selecttable
    },
    login(state) {
      state.isLogin = true
      state.id=1
      state.account=5
      state.name='lulu'
      state.avatar='../assets/img/V.png'
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
