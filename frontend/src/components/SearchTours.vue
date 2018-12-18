<template>
  <div class="searchTours">
    <div class="searchTours__wrapper">
      <label>
        Откуда
        <input type="text" v-model="from" list="cities">
      </label>

      <datalist id="cities">
        <option>Москва</option>
        <option>Санкт-Петербург</option>
        <option>Екатеринбург</option>
        <option>Новосибирск</option>
        <option>Самара</option>
      </datalist>

      <div class="arrow">
        <img src="@/assets/long-arrow-alt-right-solid.svg" alt>
      </div>
      <label>
        Куда
        <input type="text" v-model="to" list="countries">
      </label>

      <datalist id="countries">
        <option v-for="country in countries" :key="country.id">{{country.nameCountry}}</option>
      </datalist>
    </div>

    <div class="searchTours__wrapper">
      <label>
        Дата вылета
        <input type="date" v-model="dateStart">
      </label>
      
      <label>
        Прилёт
        <input type="date" v-model="dateEnd" :min="dateStart">
      </label>
    </div>

    <button class="btn" @click="getTours">Найти туры</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      from: "Москва",
      to: "",
      dateStart: "",
      dateEnd: "",
      countNight: 1,
      countries: []
    };
  },

  mounted() {
    axios
      .get("https:/dyakushev.ru/api/countries")
      .then(resp => (this.countries = resp.data.countries));

    axios
      .get("https:/dyakushev.ru/api/tours")
      .then(resp => this.$store.commit("ADD_TOURS", resp.data.tours))
  },

  methods: {
    getTours() {
      axios
        .get("https:/dyakushev.ru/api/findTours", {
          params: {
            country: this.to,
            dateStart: this.dateStart,
            dateEnd: this.dateEnd
          }
        })
        .then(resp => this.$store.commit("ADD_TOURS", resp.data.tours));
    }
  }
};
</script>

<style lang="scss" scoped>
.searchTours {
  display: flex;
  justify-content: center;
  margin: 0 auto;

  &__wrapper {
    display: flex;
  }
}

label {
  display: flex;
  flex-direction: column;

  margin-right: 20px;

  text-align: left;
  color: #000;
  font-size: 14px;

  input {
    border: 1px solid rgba(0, 115, 255, 0.3);
    box-shadow: none;
    line-height: 18px;
    padding: 10px;
    height: 40px;
    min-height: 40px;
    box-sizing: border-box;
    background: #fff;
    border-radius: 3px;
    overflow: hidden;
    outline: none;
    color: #000;
    background-clip: padding-box;

    margin-top: 5px;
  }
}

.arrow {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 20px;
  margin-right: 20px;

  img {
    height: 20px;
  }
}

.btn {
  margin: auto 0 0 0;
  height: 40px;
  background-color: #fff;
  color: #0073ff;
  cursor: pointer;
  border: none;
  border-radius: 3px;
  border: 1px solid rgba(0, 115, 255, 0.3);
}
</style>