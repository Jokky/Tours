<template>
  <section class="cart">
    <div class="carousel">
      <div class="btn-slide" @click="prevImage">
        <img src="@/assets/angle-left-solid.svg" alt>
      </div>
      <img :src="getCurrentImage" alt class="image">
      <div class="btn-slide btn-slide--right" @click="nextImage">
        <img src="@/assets/angle-left-solid.svg" alt>
      </div>
    </div>
    <div class="cart__info">
      <span class="cart__info__name">{{tour.nameHotel}}</span>
      <span class="cart__info__country">{{tour.nameCountry}}</span>
      <div class="cart__info__wrapper">
        <label>
          Дата вылета
          <span>{{tour.dateStart | formatDate}}</span>
        </label>
        <label>
          Дата прилета
          <span>{{tour.dateEnd | formatDate}}</span>
        </label>
      </div>
    </div>
    <div class="cart__price">
      <label>
        Цена
        <span class="tour-price">{{tour.price}} руб.</span>
      </label>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  props: {
    tour: {
      type: Object
    }
  },

  data() {
    return {
      posCurImage: 0,
      images: []
    };
  },

  methods: {
    prevImage() {
      this.posCurImage <= 0 ? this.posCurImage : this.posCurImage--;
    },
    nextImage() {
      this.posCurImage >= this.images.length - 1
        ? this.posCurImage
        : this.posCurImage++;
    }
  },

  computed: {
    getCurrentImage() {
      if (this.images.length > 0) 
        return this.images[this.posCurImage].urlImage;
      else 
        return null
    }
  },

  mounted() {
    axios
      .get("https:/dyakushev.ru/api/getImagesHotel", {
        params: {
          hotel_id: this.tour.idHotel
        }
      })
      .then(resp => (this.images = resp.data.images));
  }
};
</script>

<style lang="scss" scoped>
.carousel {
  position: relative;

  .btn-slide {
    opacity: 0;
    position: absolute;
    width: 40px;
    top: 0;
    bottom: 0;
    background: linear-gradient(to right, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0));

    display: flex;
    justify-content: center;

    &--right {
      right: 0;
      transform: rotate(-180deg);
    }

    img {
      width: 20px;
      opacity: 0.7;
    }
  }

  &:hover {
    .btn-slide {
      opacity: 1;
    }
  }

  .image {
    width: 200px;
    height: 100%;
    object-fit: cover;
  }
}

.cart {
  width: 100%;
  border-radius: 3px;
  border: 1px solid rgba(0, 0, 0, 0.1);

  display: flex;

  text-align: left;

  &__info {
    display: flex;
    flex-direction: column;
    padding: 20px;

    &__name {
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 12px;
    }

    &__country {
      font-size: 16px;
      margin-bottom: 24px;
    }

    &__wrapper {
      display: flex;
    }

    label {
      text-align: left;
      display: flex;
      flex-direction: column;
      margin-right: 30px;
      color: rgba(0, 0, 0, 0.5);

      span {
        color: #000;
        font-size: 18px;
        font-weight: 500;
      }
    }
  }

  &__price {
    display: flex;
    width: 20%;
    justify-content: center;
    align-items: center;
    margin: 0 0 0 auto;
    padding: 15px;
    border-left: 1px solid rgba(0, 0, 0, 0.1);

    label {
      display: flex;
      flex-direction: column;
      color: rgba(0, 0, 0, 0.5);

      span {
        margin-top: 3px;
        color: #000;
        font-size: 24px;
      }
    }
  }
}
</style>