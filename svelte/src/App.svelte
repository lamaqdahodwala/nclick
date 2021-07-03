<script>
	import BuyAuto from './BuyAuto.svelte'
	import { pts, cps } from './stores.js'
	let modalOpen = false
</script>

<main>
	<div class="container">
		<h1 class="title">{$pts}</h1>
		<h1 class="subtitle">{$cps}</h1>
		<br><br>

		<BuyAuto name='yeet' amount=15 cost=1/>
	</div>
</main>

