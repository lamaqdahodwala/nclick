<script>
    import { pts, clicksps } from './stores.js'

    export let name;
    export let price;
    export let amount
    
    

    function buy(){
        if ($pts >= price){
            pts.set(($pts - price))
            clicksps.set($clicksps + parseInt(amount))
            // alert($pts)
            // alert($clicksps)
        } else {
            alert("You can't buy this!")
        }
    }
</script>

<button on:click={buy} class="button is-{$pts >= price ? 'success' : 'warning'}">
    Buy {name} for {price}
</button>