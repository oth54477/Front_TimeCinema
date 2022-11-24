<template>
  <section class="search-body">
    <DetailModal v-if="modal" :id="movieId"  @close="closeModal"/>
    <div class="search-bar-box">
      <input class="search-input" type="text" @input="search" @keyup.enter="searchEnter">
    </div>
    <div class="search-result-box">
      <SearchItem 
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        @movieIndex="getIndex"
      />
    </div>
  </section>
</template>

<script>
import SearchItem from '@/components/SearchItem'
import DetailModal from '@/components/DetailModal'
import axios from 'axios'
import SERVER from '@/api/drf.js'

export default {
  name: 'SearchView',
  components: {
    SearchItem,
    DetailModal,
  },
  computed: {
    modal() {
      const bodyTag = document.querySelector('body')
      const modal = this.$store.state.modal
      console.log(modal)
      if (modal === true) {
        bodyTag.style.overflow = 'hidden'
      } else {
        bodyTag.style.overflow = ''
      }
      return this.$store.state.modal
    }
  },
  data() {
    return {
      inputData: null,
      movies: null,
      movieId: null,
    }
  },
  methods: {
    search(e) {
      this.inputData = e.target.value.trim()
      console.log(this.inputData)
      axios({
        method: 'get',
        url: `https://api.themoviedb.org/3/search/movie`,
        params: {
          api_key: SERVER.TMDB_API_KEY,
          language: 'ko-KR',
          query: this.inputData,
          page: 1,
          include_adult: false,
        }
      })
        .then((res) => {
          console.log(res)
          const movies = res.data.results
          this.movies = movies.filter(movie => movie.poster_path !== null)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    searchEnter(e) {
      e.target.value = null
    },
    getIndex(index) {
      console.log(index)
      this.movieId = index
    },
    closeModal() {
      this.$store.commit('MODAL', false)
    },
  }
}
</script>
"https://api.themoviedb.org/3/search/movie?language=ko-KR&query=%EC%95%84%EC%9D%B4%EC%96%B8&page=1&include_adult=false"
https://api.themoviedb.org/3/search/movie?api_key=aa46434748a2cdd1226cec5e6f272ef5&language=ko-KR&query=%EC%95%84%EC%9D%B4%EC%96%B8%EB%A7%A8&page=1&include_adult=false
<style>
.search-body {
  position: relative;
  top: 0px;
  left: 0px;
  width: 100vw;
  height: 100vh;
  color: #1f1f1f;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: flex-end;
}

.search-bar-box {

}

.search-input {
  margin-bottom: 8vh;
  width: 30vw;
  height: 5vh;
  border-radius: 45px;
  background-color: #eae9e4;
  padding: 0px 2rem;
  font-size: 1.8rem;
}

.search-result-box {
  width: 75vw;
  height: 71vh;
  background-color: #eae9e4;
  border-radius: 15px;
  padding: 3rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  overflow: scroll;
}
</style>