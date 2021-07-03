<script>
	import { onMount } from 'svelte';

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
		<Button on:click={handleClick} >Click for pts</Button>

		<BuyAuto name='yeet' amount=15 cost=1/>
	</div>
</main>

