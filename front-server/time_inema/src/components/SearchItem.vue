<template>
  <section class="search-item-body" @click="goToDetail">
    <div>
      <img class="search-img" :src="`https://www.themoviedb.org/t/p/original${movie.poster_path}`">
      <div class="cover"><span>{{ movie.title }}</span></div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'SearchItem',
  props: {
    movie: Object,
  },
  methods: {
    goToDetail() {
      console.log(1)
      this.$store.commit('MODAL', true)
      this.$emit('movieIndex', this.movie.id)
    }
  }
}
</script>

<style>
.search-item-body {
  width: 10vw;
  margin: 1rem 1rem;
  cursor: pointer;
}

.search-item-body:hover {
  transition: transform .2s;
  transform: scale(1.2);
}

.search-item-body:hover .cover {
  animation: info 1.5s forwards ;
}

@keyframes info {
  0% {

  }
  100% {
    opacity: 1;
  }
}

.search-item-body > div {
  position: relative;
}

.search-img {
  border-radius: 10px;
  height: 15vw;
  width: 10vw;
}

.cover {
  width: 100%;
  height: 100%;
  border-radius: 10px !important;

  /* background-color: black; */
  background: linear-gradient(180deg, #0000003d, #201f1f);;
  position: absolute;
  top: 0px;
  left: 0px;
  opacity: 0;
  z-index: 50;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}

.cover > span {
  /* margin-top: 5vw; */
  margin-bottom: 4vw;
  font-size: 20px;
  font-weight: 600;
  color: white;
}
</style>