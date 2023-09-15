<template>

  <div class="project" >
    <div class="actions">

      <tr>
        <th>  --- BTCUSDT --- </th>
          <br/>
        <th> Dollar Value: {{dollar_value_calculation_btc.toFixed(2)}}</th>
          <br/>
        <th> Coin Value: {{coin_value_calculation_btc.toFixed(2)}}</th>
          <br/>
        <th> Last Price BTCUSDT: {{last_price_coin.BTCUSDT}}</th>
          <br/>
        <th> Asset Value: {{asset_value_btc.toFixed(2)}}</th>
          <br/>
        <th> Balance Sheet : {{balance_sheet_btc.toFixed(2)}}</th>
      </tr>

            <div class="icons">
               <span  @click="HandleRefresh" class="material-icons">refresh</span>
            </div>

    </div>
  </div>
    <div class="project" >
    <div class="actions">
      <tr>
        <th>  --- ETHUSDT --- </th>
          <br/>
        <th> Dollar Value: {{dollar_value_calculation_eth.toFixed(2)}}</th>
          <br/>
        <th> Coin Value: {{coin_value_calculation_eth.toFixed(2)}}</th>
          <br/>
        <th> Last Price ETHUSDT: {{last_price_coin.ETHUSDT}}</th>
          <br/>
        <th> Asset Value: {{asset_value_eth.toFixed(2)}}</th>
          <br/>
        <th> Balance Sheet : {{balance_sheet_eth.toFixed(2)}}</th>
      </tr>

      <div class="icons">
         <span  @click="HandleRefresh" class="material-icons">refresh</span>
      </div>

    </div>
  </div>

</template>

<script >
import axios from "axios";

export default {
  props: ['projects'],
  data(){
    return{
      last_price_coin:0.0,

      dollar_value_calculation_btc:0.0,
      coin_value_calculation_btc: 0.0,
      asset_value_btc:0.0,
      balance_sheet_btc:0.0,

      dollar_value_calculation_eth:0.0,
      coin_value_calculation_eth: 0.0,
      asset_value_eth:0.0,
      balance_sheet_eth:0.0,

      balanceSheet: {},


    }
  },
  mounted() {
    this.HandleRefresh()
  },
  methods: {
    HandleRefresh() {
      axios
          .get("http://127.0.0.1:8000//exchange/lastPriceApi")
          .then(response => {
            this.last_price_coin = response.data
            console.log(this.last_price_coin.BTCUSDT)
            console.log(this.last_price_coin.BTCUSDT)
            console.log(this.last_price_coin.BTCUSDT)
            console.log(this.last_price_coin.BTCUSDT)
            this.HandelFor()
            // this.calculateBalanceSheet()
          })
    },
    HandelFor() {
      this.handelZero()
      for (const project of this.projects) {

        if (project.currency == 'BTCUSDT') {
          if (project.type_position === 'sell') {
            this.dollar_value_calculation_btc -= parseFloat(project.dollar_value)
            this.coin_value_calculation_btc -= parseFloat(project.coin_value)
          } else if (project.type_position === 'buy') {
            this.dollar_value_calculation_btc += parseFloat(project.dollar_value)
            this.coin_value_calculation_btc += parseFloat(project.coin_value)
          }

          this.asset_value_btc = this.last_price_coin.BTCUSDT * this.coin_value_calculation_btc
          this.balance_sheet_btc = this.asset_value_btc - this.dollar_value_calculation_btc

        }

        if (project.currency == 'ETHUSDT') {
          if (project.type_position === 'sell') {
            this.dollar_value_calculation_eth -= parseFloat(project.dollar_value)
            this.coin_value_calculation_eth -= parseFloat(project.coin_value)
          } else if (project.type_position === 'buy') {
            this.dollar_value_calculation_eth += parseFloat(project.dollar_value)
            this.coin_value_calculation_eth += parseFloat(project.coin_value)
          }


          this.asset_value_eth = this.last_price_coin.ETHUSDT * this.coin_value_calculation_eth
          this.balance_sheet_eth = this.asset_value_eth - this.dollar_value_calculation_eth
        }
      }
    },
    handelZero(){
      this.dollar_value_calculation_btc= 0.0
      this.coin_value_calculation_btc=  0.0
      this.asset_value_btc= 0.0
      this.balance_sheet_btc= 0.0

      this.dollar_value_calculation_eth= 0.0
      this.coin_value_calculation_eth=  0.0
      this.asset_value_eth= 0.0
      this.balance_sheet_eth= 0.0
    },


    calculateBalanceSheet() {
    const balanceSheet = {};

    for (const project of this.projects) {
      const currency = project.currency;

      if (!balanceSheet[currency]) {
        balanceSheet[currency] = {};
        balanceSheet[currency].dollarValue = 0
        balanceSheet[currency].coinValue = 0
      }
      if (project.type_position === "sell") {
        balanceSheet[currency].dollarValue -= parseFloat(project.dollar_value);
        balanceSheet[currency].coinValue -= parseFloat(project.coin_value);
      }
      else {
        balanceSheet[currency].dollarValue += parseFloat(project.dollar_value);
        balanceSheet[currency].coinValue += parseFloat(project.coin_value);
      }
      console.log(currency)
      balanceSheet[currency].assetValue = 0
      balanceSheet[currency].balanceSheetCoin = 0

      balanceSheet[currency].assetValue = balanceSheet[currency].coinValue * this.last_price_coin[currency];
      balanceSheet[currency].balanceSheetCoin = balanceSheet[currency].assetValue - balanceSheet[currency].dollarValue;
    }

    this.balanceSheet= balanceSheet;

    console.log(balanceSheet['BTCUSDT'].dollarValue)
    console.log(balanceSheet['BTCUSDT'].coinValue)
    console.log(balanceSheet['BTCUSDT'].assetValue)
    console.log(balanceSheet['BTCUSDT'].balanceSheetCoin)

    console.log(balanceSheet['ETHUSDT'].dollarValue)
    console.log(balanceSheet['ETHUSDT'].coinValue)
    console.log(balanceSheet['ETHUSDT'].assetValue)
    console.log(balanceSheet['ETHUSDT'].balanceSheetCoin)


    this.balanceSheet= balanceSheet;
     }
    }
}
</script>



<style scoped >

td, th {
  //border: 1px solid #dddddd;
  text-align: left;
  width: 310px;
}


</style>
