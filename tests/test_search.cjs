'use strict';
const test=require('node:test'),assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path');
const search=require('../docs/catalog-engine.js'),data={projects:Array.from({length:JSON.parse(fs.readFileSync(path.join(__dirname,'../docs/catalog.json'),'utf8')).shards.length},(_,i)=>JSON.parse(fs.readFileSync(path.join(__dirname,'../docs/catalog-'+i+'.json'),'utf8'))).flat()};
test('literal conjunctive matching agrees with independent per-field oracle',()=>{
 const queries=['rank fusion','source prefixes','signed postings','implicit zero','occurrence quotas','finite suppression','interval retention','residual reduced','DFA conditioning','future mass','retry risk','completion law','occurrence indexing','overlapping frequency','block buckets','posting visits','finite retry','proposal grid','activation integer','partial accumulator','joint deletion','singleton extrapolation','factor membership','optimal set index','fooling set','rectangle cover','empty threat','contingent plan','skipped variable','hidden extension','token balance','firing multiset','','ctc','FAIRNESS','exact rational','retrieval','not-a-real-project','[a-z]','<script>','a+b','conditioned transition','  CTC   prefix  ','fair justice','bundle menus','seller coalition'];
 for(const query of queries){
  const words=query.normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase().trim().split(/\s+/).filter(Boolean);
  const expected=data.projects.filter(p=>{const text=[p.id,p.title,p.excerpt,...p.headings,...(p.terms||[])].join(' ').normalize('NFKD').replace(/\p{M}/gu,'').toLowerCase();return words.every(w=>text.indexOf(w)!==-1);}).map(p=>p.id);
  assert.deepEqual(search.select(data.projects,query).map(p=>p.id),expected,query);
 }
 for(const q of['rank fusion','source prefixes'])assert.ok(search.select(data.projects,q).some(p=>p.id==='retrievalbench'));
 for(const q of['signed postings','implicit zero'])assert.ok(search.select(data.projects,q).some(p=>p.id==='ragline'));
 for(const q of['token balance','firing multiset'])assert.ok(search.select(data.projects,q).some(p=>p.id==='firelab'));
 for(const q of['unsupported frontier','whole path lottery'])assert.ok(search.select(data.projects,q).some(p=>p.id==='paretolab'));
 for(const q of['bundle menus','seller coalition'])assert.ok(search.select(data.projects,q).some(p=>p.id==='auctionlab'));
 for(const q of['occurrence indexing','overlapping frequency'])assert.ok(search.select(data.projects,q).some(p=>p.id==='tokenforge'));
 for(const q of['DFA conditioning','future mass'])assert.ok(search.select(data.projects,q).some(p=>p.id==='structgate'));
 for(const q of['retry risk','completion law'])assert.ok(search.select(data.projects,q).some(p=>p.id==='planbench'));
 for(const q of['interval retention','residual reduced'])assert.ok(search.select(data.projects,q).some(p=>p.id==='agenttrace'));
 for(const q of['occurrence quotas','finite suppression'])assert.ok(search.select(data.projects,q).some(p=>p.id==='promptguard'));
 assert.ok(search.select(data.projects,'ctc').some(p=>p.id==='ctclab'));
 assert.ok(search.select(data.projects,'fairness').some(p=>p.id==='branchlab'));
});
test('accent normalization, empty query and exact source order',()=>{
 assert.equal(search.fold('CAFÉ'),'cafe');assert.equal(search.fold('Cafe\u0301'),'cafe');
 assert.deepEqual(search.select(data.projects,''),data.projects);
 assert.deepEqual(search.select(data.projects,'   '),data.projects);
 assert.deepEqual(search.select([{id:'cafe',title:'Café',excerpt:'',headings:[]}],'CAFE').map(p=>p.id),['cafe']);
});
