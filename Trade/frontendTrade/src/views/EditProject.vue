<template>
  <form @submit.prevent="handleEdit" >
   <label>entry date:</label>
    <input v-model="entry_date" type="date" required>
    <label>type position:</label>
<!--    <input v-model="type_position" type="checkbox">-->
    <select v-model="type_position">
      <option value="buy"> Buy </option>
      <option value="sell"> Sell </option>
    </select>
    <label>currency:</label>
<!--    <input v-model="currency">-->
    <select v-model="currency">
      <option value="BTCUSDT"> BTCUSDT </option>
      <option value="ETHUSDT"> ETHUSDT </option>
    </select>
    <label>entry_price:</label>
    <input v-model="entry_price" type="number">
    <label>dollar_value:</label>
    <input v-model="dollar_value" type="number">
    <label>coin_value:</label>
    <input v-model="coin_value" type="number" step="0.00001">
    <label>notes:</label>
    <input v-model="notes"   >
    <button> EDIT </button>
  </form>
</template>

<script >
import axios from "axios";

export default {
  props: ['id'],
  data() {
    return {

      entry_date: '',
      type_position: false,
      currency:'',
      entry_price:'',
      dollar_value:'',
      coin_value:'',
      notes:'',

      uri: "http://127.0.0.1:8000//portfolio/api/" + this.id +'/',
      project:[]
    }
  },
  mounted() {
        axios
        .get(this.uri )
        .then(response => {
          let data = response.data
          this.project = data
          this.entry_date = data.entry_date
          this.type_position = data.type_position
          this.currency = data.currency
          this.entry_price = data.entry_price
          this.dollar_value = data.dollar_value
          this.coin_value = data.coin_value
          this.notes = data.notes
          console.log(this.project )
        }).catch(err => console.log(err.message))
  },

  methods: {
    // handleEdit(){
    //   fetch(this.uri,{
    //     method:"PATCH",
    //     headers:{ 'content-Type': 'application/json'},
    //     body: JSON.stringify({film: this.film , director:this.director, year:this.year})
    //   }).then(() => {
    //      this.$router.push('/')
    //   }).catch(err => console.log(err.message))
    // }


    handleEdit(){
       let project = {
          entry_date: this.entry_date,
          type_position: this.type_position,
          currency: this.currency,
          entry_price: this.entry_price,
          dollar_value: this.dollar_value,
          coin_value: this.coin_value,
          notes: this.notes,
      }
      console.log(project)

      axios
          .patch(this.uri   , project )
          .then(() => {
            this.$router.push('/')
          } )
          .catch(err => console.log(err.message))

    }



    // handleEdit() {
    //
    //   axios({
    //     method: 'PATCH',
    //     url: this.uri + ,
    //     id:this.id,
    //     data: {
    //       film: this.film,
    //       director: this.director,
    //       year: this.year,
    //     }
    //   })
    // }



  }

}
</script>


<style scoped>

</style>