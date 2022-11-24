import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import TimeLineView from '@/views/TimeLineView'
import RecommendView from '@/views/RecommendView'
import ProfileView from '@/views/ProfileView'
import UserListView from '@/views/UserListView'
import EndingView from '@/views/EndingView'
import SearchView from '@/views/SearchView'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/time',
    name: 'time',
    component: TimeLineView
  },
  {
    path: '/recommend/:times',
    name: 'recommend',
    component: RecommendView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/userList',
    name: 'userList',
    component: UserListView
  },
  {
    path: '/ending',
    name: 'ending',
    component: EndingView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
