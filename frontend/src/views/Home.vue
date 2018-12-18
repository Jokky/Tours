<template>
<div class="home">
  <header class="search">
    <h1 class="title">Поиск туров 🚀</h1>
    <SearchTours></SearchTours>
  </header>
  <body class="result">
    <h1 class="nofound" v-if="!tours">Ничего не найдено</h1>
    <Cart v-else v-for="tour in tours" :key="tour.id" :tour="tour"></Cart>
  </body>
  <footer>
    <button @click="printPage">Печать</button>
  </footer>
</div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "home",
  components: {
    SearchTours: () => import("@/components/SearchTours.vue"),
    Cart: () => import("@/components/Cart.vue")
  },

  computed: {
    ...mapGetters({
      tours: "getTours"
    })
  },

  methods: {
    printPage() {
      window.print();
    }
  }
};
</script>

<style lang="scss" scoped>
.home {
  min-height: 100vh;
  width: 100%;
}

.result {
  max-width: 907px;
  margin: 30px auto;
  display: grid;
  grid-template-areas: "cart";
  grid-column-gap: 30px;
  grid-row-gap: 30px;
  grid-row-start: 30px;
}

.nofound {
  font-size: 24px;
}

.search {
  height: 300px;
  width: 100%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  background-color: rgba(0, 0, 0, 0.02);
}

.title {
  display: block;
  max-width: 907px;
  width: 100%;
  font-size: 36px;
  text-align: left;
  margin: 0;
  margin-bottom: 1rem;
}
</style>

