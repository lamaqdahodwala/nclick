<script>
    import { Modal, Button, Dialog } from 'attractions'
    import {pts, cps} from './stores.js'
    export let cost;
    export let amount;
    export let name;
    let modalOpen = false

    function purchaseAuto(){
        if ($pts < cost){
            modalOpen = true
        } else {
            pts.update(n => n-cost)
            cps.update(n => n+parseInt(amount))
        }
    }
</script>

<main>
    <Button on:click={purchaseAuto} outline noRipple>
        Buy {name} for {cost}
    </Button>
    <Modal bind:open={modalOpen} let:closeCallback>
        <Dialog title="You can't buy this!" {closeCallback}>
            Save up {cost-$pts} to buy this.
        </Dialog>
    </Modal>
    <br><br>
</main>