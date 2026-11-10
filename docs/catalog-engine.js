/* Pure matching: literal words, no regex evaluation or network access. */
(function(root){
 'use strict';
 function fold(value){return String(value).normalize('NFKD').replace(/\p{M}/gu,'').toLocaleLowerCase('en-US');}
 function words(query){return fold(query).trim().split(/\s+/u).filter(Boolean);}
 function matches(project,query){const hay=fold([project.id,project.title,project.excerpt,...project.headings,...(project.terms||[])].join(' '));return words(query).every(word=>hay.includes(word));}
 function select(projects,query){return projects.filter(p=>matches(p,query));}
 const api={fold,words,matches,select};
 if(typeof module==='object'&&module.exports)module.exports=api;
 else root.CatalogSearch=api;
})(globalThis);
