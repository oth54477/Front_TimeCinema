<template>
  <section class="music-player-body">
    <div class="fa fa-solid fa-headphones audio-btn" @click="toggleAudio" :class="{ isHome : isHome }"></div>
    <!-- <audio src="../assets/music/A Lovely Night-라라랜드.mp3" autoplay loop controls id="myAudio">오디오 지원되지 않는 브라우저</audio> -->
    <audio id="myaudio" autoplay loop controls v-show="isShow">
      <source id="main">
      <source src="../assets/music/le festin paroles-라따뚜이.mp3">
      <source src="../assets/music/Another Day Of Sun-라라랜드.mp3">
      <source src="../assets/music/Falling Slowly-원스.mp3">
      <source src="../assets/music/A Lovely Night-라라랜드.mp3">
      <source src="../assets/music/Cant Help Falling In Love-티파니에서 아침을.mp3">
      <source src="../assets/music/How long will I love you-어바웃 타임.mp3">
      <source src="../assets/music/Love Thema-시네마 천국.mp3">
      <source src="../assets/music/Love Me Like You Do-그레이의 50가지 그림자.mp3">
      <source src="../assets/music/인생의 회전목마-하울의 움직이는 성.mp3">
      <source src="../assets/music/You Need Is Love-Love Actually.mp3">
      <source src="../assets/music/My Heart Will Go On-타이타닉.mp3">
      <source src="../assets/music/Youve Got a Friend in Me-토이스토리.mp3">
      <source src="../assets/music/Whitney Houston  I Will Always Love You-보디가드.mp3">
      <source src="../assets/music/Unchained Melody-사랑과 영혼.mp3">
      <source src="../assets/music/She-노팅힐.mp3">
      <!-- <source src="http://upload.wikimedia.org/wikipedia/commons/3/32/C-major.ogg">
      <source src="http://upload.wikimedia.org/wikipedia/commons/4/4b/D-major.ogg"> -->
    </audio>
  </section>
</template>

<script>
export default {
  name: 'MusicPlayer',
  computed: {
    // OSTs() {
    //   return this.$store.state.OSTs
    // },
      // isMusic() {
      //   const isHome = location.pathname === '/'
      //   if (!isHome && this.isShow) {
      //     return true
      //   } else {
      //     return false
      //   }
      // }

    },
  data() {
    return {
      isShow: false,
      isHime: false,

    }
  },
  methods: {
    toggleAudio() {
      this.isShow = !this.isShow
    }
  },
  created() {
    if (location.pathname === '/') {
      this.isHome =  true
    } else {
      this.isHome = false
    }
  },
  updated() {
    if (location.pathname === '/') {
      this.isHome =  true
    } else {
      this.isHome = false
    }
  }
}
</script>

<style>
.music-player-body {
  position: absolute;
  z-index: 999;
  right: 1vh;
  top: 1vh;
}

#myaudio {
  position: absolute;
  top: 0px;
  left: 0px;
  z-index: 999;
  top: 4vh;
  left: -13.7vw;
}

.audio-btn {
  font-size: 2rem;

}

.isHome {
  opacity: 0;
}
</style>