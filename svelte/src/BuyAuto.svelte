<script>
    import { pts, clicksps } from './stores.js'

    export let name;
    export let price;
    export let amount
    
    

    function buy(){
        if ($pts >= price){
            pts.set(($pts - price))
            clicksps.set($clicksps + amount)
        } else {
            alert("You can't buy this!")
        }
    }
</script>

<button>
    Buy {name} for {price}
</button>