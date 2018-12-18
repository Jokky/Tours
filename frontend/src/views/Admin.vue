<template>
  <section class="addTour">
    <h1>Добавить тур</h1>
    <label>
      Начало
      <input type="date" v-model="dateStart">
    </label>
    <label>
      Конец
      <input type="date" v-model="dateEnd" :min="dateStart">
    </label>
    
    <label>
      Отель
      <input type="text" v-model="hotel" list="hotels">
    </label>

    <datalist id="hotels">
      <option v-for="hotel in hotels" :key="hotel.id">{{hotel.nameHotel}}</option>
    </datalist>

    <label>
      Цена
      <input type="number" v-model="price" min="0">
    </label>
    
    <button class="btn" @click="uploadTour">Сохранить</button>
  </section>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dateStart: "",
      dateEnd: "",
      country: "",
      countries: [],
      hotels: [],
      price: 0,
      hotel: "",
      imageUrl:
        "https://media-cdn.tripadvisor.com/media/photo-s/0f/4c/19/17/mercure-hotel-moa-berlin.jpg"
    };
  },

  mounted() {
    axios
      .get("https:/dyakushev.ru/api/countries")
      .then(resp => (this.countries = resp.data.countries));

    axios
      .get("https:/dyakushev.ru/api/hotels")
      // .then(resp => console.log(resp))
      .then(resp => (this.hotels = resp.data.hotels));
  },

  methods: {
    uploadTour() {
      axios.get("https:/dyakushev.ru/api/addTour", {
        params: {
          idHotel: this.hotels.find(item => item.nameHotel == this.hotel)
            .idHotel,
          dateStart: this.dateStart,
          dateEnd: this.dateEnd,
          price: this.price
        }
      })
      .then( () => {
        alert('Тур добавлен')
        this.dateStart = ''
        this.dateEnd = ''
        this.price = ''
        this.hotel = ''
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.addTour {
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 300px;
  height: 100vh;
  margin: auto;
}

h1 {
  font-size: 24px;
}

label {
  display: flex;
  flex-direction: column;

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

    margin: 5px 0 20px 0;
  }
}

.btn {
  padding: 10px;
  background-color: #fff;
  color: #0073ff;
  cursor: pointer;
  border: none;
  border-radius: 3px;
  border: 1px solid rgba(0, 115, 255, 0.3);
}
</style>