<script>
	import { onMount } from 'svelte';
	import {Button} from 'attractions'
	import BuyAuto from './BuyAuto.svelte'
	import { pts, cps } from './stores.js'
	let modalOpen = false
	

	function handleClick(){
		pts.update((n) => n+1)
	}

	onMount(() => {
		let loop = setInterval(() =>{
			pts.update(n => n+$cps)
		}, 1000)
	})
</script>

<main>
	<div class="container">
		<h1 class="title">{$pts}</h1>
		<h1 class="subtitle">{$cps}</h1>
		<br><br>
		<Button on:click={handleClick} outlined filled >Click for pts</Button>
		<br><br>
		<BuyAuto name='yeet' amount=15 cost=1/>
	</div>
</main>

