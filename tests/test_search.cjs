'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const search=require('../docs/catalog-engine.js'),data={projects:Array.from({length:JSON.parse(fs.readFileSync(path.join(__dirname,'../docs/catalog.json'),'utf8')).shards.length},(_,i)=>JSON.parse(fs.readFileSync(path.join(__dirname,'../docs/catalog-'+i+'.json'),'utf8'))).flat()};
test('literal conjunctive matching agrees with independent per-field oracle',()=>{
 const queries=['activation integer','partial accumulator','joint deletion','singleton extrapolation','factor membership','optimal set index','fooling set','rectangle cover','empty threat','contingent plan','skipped variable','hidden extension','token balance','firing multiset','','ctc','FAIRNESS','exact rational','retrieval','not-a-real-project','[a-z]','<script>','a+b','conditioned transition','  CTC   prefix  ','fair justice','bundle menus','seller coalition'];
 for(const query of queries){
  const words=query.normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase().trim().split(/\s+/).filter(Boolean);
  const expected=data.projects.filter(p=>{const text=[p.id,p.title,p.excerpt,...p.headings,...(p.terms||[])].join(' ').normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase();return words.every(w=>text.indexOf(w)!==-1);}).map(p=>p.id);
  assert.deepEqual(search.select(data.projects,query).map(p=>p.id),expected,query);
 }
 for(const q of['token balance','firing multiset'])assert.ok(search.select(data.projects,q).some(p=>p.id==='firelab'));
 for(const q of['unsupported frontier','whole path lottery'])assert.ok(search.select(data.projects,q).some(p=>p.id==='paretolab'));
 for(const q of['bundle menus','seller coalition'])assert.ok(search.select(data.projects,q).some(p=>p.id==='auctionlab'));
 assert.ok(search.select(data.projects,'ctc').some(p=>p.id==='ctclab'));
 assert.ok(search.select(data.projects,'fairness').some(p=>p.id==='branchlab'));
});
test('accent normalization, empty query and exact source order',()=>{
 assert.equal(search.fold('CAFÉ'),'cafe');assert.equal(search.fold('Cafe\u0301'),'cafe');
 assert.deepEqual(search.select(data.projects,''),data.projects);
 assert.deepEqual(search.select(data.projects,'   '),data.projects);
 assert.deepEqual(search.select([{id:'cafe',title:'Café',excerpt:'',headings:[]}],'CAFE').map(p=>p.id),['cafe']);
});
