/* Progressive enhancement: the generated source list also works without JS. */
(function(){
 'use strict';
 const input=document.getElementById('query'),count=document.getElementById('count'),form=document.getElementById('search-form'),empty=document.getElementById('empty');
 const data=globalThis.PORTFOLIO_CATALOG,engine=globalThis.CatalogSearch;
 if(!data||!engine)return;
 const cards=new Map([...document.querySelectorAll('.project')].map(card=>[card.dataset.id,card]));
 if(cards.size!==data.projects.length||data.projects.some(p=>!cards.has(p.id)))return;
 function render(save){
  const query=input.value.slice(0,256);if(query!==input.value)input.value=query;
  const found=new Set(engine.select(data.projects,query).map(p=>p.id));
  for(const [id,card]of cards)card.hidden=!found.has(id);
  count.textContent=found.size+' of '+data.projects.length+' case studies'+(query.trim()?' match.':', in project ID order.');
  empty.hidden=found.size!==0;
  if(save){const url=new URL(location.href);if(query)url.searchParams.set('q',query);else url.searchParams.delete('q');history.replaceState(null,'',url);}
 }
 function restore(){input.value=(new URL(location.href).searchParams.get('q')||'').slice(0,256);render(false);}
 form.hidden=false;restore();input.addEventListener('input',()=>render(true));
 form.addEventListener('submit',event=>{event.preventDefault();render(true);});
 document.getElementById('clear').addEventListener('click',()=>{input.value='';render(true);input.focus();});
 addEventListener('popstate',restore);
})();
