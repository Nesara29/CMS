<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>College Management System · 3D VFX</title>
<style>
:root{--bg:#0b132b;--panel:rgba(28,37,65,.9);--fg:#F1F5F9;--mut:#9aa7c0;--ac:#5BC0BE}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0b132b}}
:root[data-theme="dark"]{--bg:#0b132b}
html,body{height:100%;margin:0;padding:0;background:var(--bg)}
body{color:var(--fg);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;overflow:hidden}
canvas{display:block;position:fixed;inset:0;touch-action:none}
.top{position:fixed;top:0;left:0;right:0;z-index:5;box-sizing:border-box;padding:calc(env(safe-area-inset-top,0px) + 20px) 22px 14px;pointer-events:none;background:linear-gradient(var(--bg),transparent);border:0}
.ttl{margin:0;font-size:clamp(18px,3.2vw,30px);font-weight:700;letter-spacing:.04em;line-height:1.2}
.sub{margin:6px 0 0;color:var(--mut);font-size:13px}
.panel{position:fixed;right:18px;top:100px;z-index:6;box-sizing:border-box;width:min(340px,calc(100% - 36px));background:var(--panel);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.12);border-radius:14px;padding:16px 18px;display:none;box-shadow:0 0 40px -10px var(--glow,#5BC0BE)}
.panel.in{animation:pop .45s cubic-bezier(.2,1.4,.4,1)}
@keyframes pop{from{opacity:0;transform:translateY(14px) scale(.96)}to{opacity:1;transform:none}}
.panel .tag{color:var(--glow,var(--ac));font-size:12px;font-weight:600}
.panel .name{margin:4px 0 0;font-size:17px;font-weight:700}
.panel .desc{margin:10px 0;font-size:14px;line-height:1.5}
.panel .run{background:rgba(0,0,0,.35);padding:8px 10px;border-radius:8px;font:12px/1.5 ui-monospace,Consolas,monospace;overflow-x:auto;white-space:pre}
.panel .close{position:absolute;top:6px;right:10px;background:none;border:0;color:var(--mut);font-size:22px;cursor:pointer}
.chips{position:fixed;left:0;right:0;bottom:0;z-index:5;box-sizing:border-box;display:flex;gap:8px;overflow-x:auto;padding:12px 18px calc(env(safe-area-inset-bottom,0px) + 12px)}
.chips button{flex:none;background:var(--panel);color:var(--fg);border:1px solid rgba(255,255,255,.14);border-radius:999px;padding:7px 14px;font-size:13px;cursor:pointer;transition:.25s}
.chips button.on{background:var(--ac);border-color:var(--ac);color:#0b132b;box-shadow:0 0 18px var(--ac)}
button:focus-visible{outline:3px solid var(--ac);outline-offset:2px}
.hint{position:fixed;left:22px;bottom:70px;color:var(--mut);font-size:12px;pointer-events:none}
</style>
</head>
<body>
<div class="top"><div class="ttl">COLLEGE MANAGEMENT SYSTEM</div><div class="sub">Flask · SQLAlchemy · MySQL · Role-Based Access — drag to orbit, click a node, click space for a shockwave</div></div>
<div class="panel" id="panel"><button class="close" id="x" aria-label="Close">×</button><div class="tag" id="pt"></div><div class="name" id="pn"></div><div class="desc" id="pd"></div><div class="run" id="pr"></div></div>
<div class="hint">Light pulses show data flowing between modules</div>
<div class="chips" id="chips"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
const TAU=Math.PI*2,AD=THREE.AdditiveBlending,reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
const C={access:0xFF4D6D,role:0x5BC0BE,acad:0xF0B429,data:0x7F5AF0,report:0x2CB67D};
const D=[
{id:'Auth',n:'Authentication & Roles',s:'Flask-Login · Role-gated routes',k:'access',d:'Secure session login. Every route is gated by role (Admin, HOD or Staff) using decorators.',r:'routes/auth_routes.py\nservices/auth_service.py\nutils/decorators.py\nmodels/user.py, role.py'},
{id:'Admin',n:'Admin Dashboard',s:'Role: Admin',k:'role',d:'User and role management, system settings, and database backup and restore.',r:'routes/admin_routes.py\ntemplates/admin.html\ntemplates/manage_users.html'},
{id:'HOD',n:'HOD Dashboard',s:'Role: HOD',k:'role',d:'HODs allocate subjects and classes to staff and review department reports.',r:'routes/hod_routes.py\ntemplates/hod.html'},
{id:'Staff',n:'Staff Dashboard',s:'Role: Staff',k:'role',d:'Staff mark attendance and manage CIE papers and marks for their allocated subjects.',r:'routes/staff_routes.py\ntemplates/staff.html'},
{id:'Attendance',n:'Attendance Tracking',s:'Service + API + Model',k:'acad',d:'Mark and track student attendance per subject and class.',r:'services/attendance_service.py\napi/attendance_api.py\nmodels/attendance.py'},
{id:'CIE',n:'CIE Management',s:'Continuous Internal Evaluation',k:'acad',d:'CIE configuration per subject, marks entry, and CIE paper uploads.',r:'services/cie_service.py\napi/cie_api.py\nmodels/cie_config.py, cie_marks.py, cie_papers.py\nuploads/cie_papers/'},
{id:'Allocation',n:'Staff Allocation',s:'Staff ↔ Subject ↔ Class',k:'acad',d:'Allocates staff to subjects and classes.',r:'services/allocation_service.py\napi/allocation_api.py\nmodels/staff_allocation.py'},
{id:'Students',n:'Academic Records',s:'Students · Batches · Branches',k:'acad',d:'Student, batch, branch, class and subject records, with bulk student upload templates.',r:'api/student_api.py\nmodels/student.py, batch.py, branch.py,\n  class_model.py, subjects.py'},
{id:'Reports',n:'PDF & Excel Reports',s:'reportlab · fpdf2 · pandas · openpyxl',k:'report',d:'Generates PDF and Excel reports from attendance and CIE data.',r:'services/report_service.py\napi/report_api.py\nutils/pdf_generator.py'},
{id:'Backup',n:'Backup & Restore',s:'.xlsx database backups',k:'report',d:'Exports the database to .xlsx backups, restores from them, and logs each backup.',r:'services/backup_service.py\napi/backup_api.py\nmodels/backup_log.py\nbackups/'},
{id:'Database',n:'Data Layer',s:'SQLAlchemy · Flask-Migrate · MySQL',k:'data',d:'All paths go through the service layer to SQLAlchemy models backed by MySQL, with Alembic migrations.',r:'flask db upgrade\nmodels/\nmigrations/'}
];
const R=new THREE.WebGLRenderer({antialias:true,alpha:true});
R.setPixelRatio(Math.min(devicePixelRatio,2));R.setSize(innerWidth,innerHeight);document.body.prepend(R.domElement);
const S=new THREE.Scene();S.fog=new THREE.FogExp2(0x0b132b,.03);
const cam=new THREE.PerspectiveCamera(55,innerWidth/innerHeight,.1,100);cam.position.set(0,2.5,reduce?14:30);
S.add(new THREE.AmbientLight(0xffffff,.55));
const pl=new THREE.PointLight(0xffffff,1.3,60);pl.position.set(6,8,8);S.add(pl);
function glowTex(){const c=document.createElement('canvas');c.width=c.height=128;const x=c.getContext('2d'),g=x.createRadialGradient(64,64,0,64,64,64);g.addColorStop(0,'rgba(255,255,255,1)');g.addColorStop(.25,'rgba(255,255,255,.35)');g.addColorStop(1,'rgba(255,255,255,0)');x.fillStyle=g;x.fillRect(0,0,128,128);return new THREE.CanvasTexture(c)}
const GT=glowTex(),pal=Object.values(C).map(h=>new THREE.Color(h));
const knot=new THREE.Mesh(new THREE.TorusKnotGeometry(1.6,.4,120,16),new THREE.MeshBasicMaterial({color:0x5BC0BE,wireframe:true,transparent:true,opacity:.45,blending:AD,depthWrite:false}));S.add(knot);
const coreGlow=new THREE.Sprite(new THREE.SpriteMaterial({map:GT,color:0x5BC0BE,transparent:true,opacity:.5,blending:AD,depthWrite:false}));coreGlow.scale.set(9,9,1);S.add(coreGlow);
const sp=new Float32Array(1500);for(let i=0;i<1500;i++)sp[i]=(Math.random()-.5)*60;
const sg=new THREE.BufferGeometry();sg.setAttribute('position',new THREE.BufferAttribute(sp,3));
const stars=new THREE.Points(sg,new THREE.PointsMaterial({color:0xF1F5F9,size:.06,transparent:true,opacity:.7}));S.add(stars);
const GN=3500,gp=new Float32Array(GN*3),gc=new Float32Array(GN*3);
for(let i=0;i<GN;i++){const r=3+Math.pow(Math.random(),.6)*20,a=Math.random()*TAU+r*.35,y=(Math.random()-.5)*(1.5+r*.12),c=pal[i%5].clone().multiplyScalar(.45+Math.random()*.55);gp.set([Math.cos(a)*r,y,Math.sin(a)*r],i*3);gc.set([c.r,c.g,c.b],i*3)}
const gg=new THREE.BufferGeometry();gg.setAttribute('position',new THREE.BufferAttribute(gp,3));gg.setAttribute('color',new THREE.BufferAttribute(gc,3));
const gal=new THREE.Points(gg,new THREE.PointsMaterial({size:.1,vertexColors:true,transparent:true,opacity:.8,blending:AD,depthWrite:false}));S.add(gal);
const G=new THREE.Group();S.add(G);
const nodes=[],nc=[];
function label(t){const c=document.createElement('canvas');c.width=256;c.height=64;const x=c.getContext('2d');x.font='600 32px system-ui,sans-serif';x.fillStyle='#F1F5F9';x.textAlign='center';x.textBaseline='middle';x.fillText(t,128,34);
const s=new THREE.Sprite(new THREE.SpriteMaterial({map:new THREE.CanvasTexture(c),transparent:true}));s.scale.set(2.4,.6,1);return s}
D.forEach((e,i)=>{
 const a=i/D.length*TAU,r=6.5,col=C[e.k];nc.push(new THREE.Color(col));
 const m=new THREE.Mesh(new THREE.IcosahedronGeometry(.7,1),new THREE.MeshStandardMaterial({color:col,roughness:.35,metalness:.3,emissive:col,emissiveIntensity:.3}));
 m.position.set(Math.cos(a)*r,Math.sin(i*1.1)*1.3,Math.sin(a)*r);
 const l=label(e.id);l.position.y=1.3;m.add(l);
 m.add(new THREE.Mesh(new THREE.IcosahedronGeometry(.95,1),new THREE.MeshBasicMaterial({color:col,wireframe:true,transparent:true,opacity:.25})));
 const gl=new THREE.Sprite(new THREE.SpriteMaterial({map:GT,color:col,transparent:true,opacity:.65,blending:AD,depthWrite:false}));gl.scale.set(3.6,3.6,1);m.add(gl);
 m.userData={i,base:m.position.y,s:1,born:reduce?0:.4+i*.14};m.scale.setScalar(.001);G.add(m);nodes.push(m);
});
/* data-flow links and travelling pulses */
const E=[[0,1],[0,2],[0,3],[3,4],[3,5],[2,6],[2,8],[1,9],[6,7],[4,10],[5,10],[7,10],[8,10],[9,10]];
const lp=new Float32Array(E.length*6),lc=new Float32Array(E.length*6),ew=E.map(()=>.5);
const lg=new THREE.BufferGeometry();lg.setAttribute('position',new THREE.BufferAttribute(lp,3));lg.setAttribute('color',new THREE.BufferAttribute(lc,3));
const lines=new THREE.LineSegments(lg,new THREE.LineBasicMaterial({vertexColors:true,transparent:true,blending:AD,depthWrite:false}));lines.frustumCulled=false;G.add(lines);
const PP=E.length*3,pp=new Float32Array(PP*3),pcl=new Float32Array(PP*3);
const pg=new THREE.BufferGeometry();pg.setAttribute('position',new THREE.BufferAttribute(pp,3));pg.setAttribute('color',new THREE.BufferAttribute(pcl,3));
const pulses=new THREE.Points(pg,new THREE.PointsMaterial({size:.5,map:GT,vertexColors:true,transparent:true,blending:AD,depthWrite:false}));pulses.frustumCulled=false;G.add(pulses);
/* shockwaves */
const waves=[];
function wave(pos,col){const m=new THREE.Mesh(new THREE.RingGeometry(.92,1,64),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:.9,side:THREE.DoubleSide,blending:AD,depthWrite:false}));m.position.copy(pos);m.lookAt(cam.position);S.add(m);waves.push({m,t:0})}
const chips=document.getElementById('chips'),panel=document.getElementById('panel');
const pt=document.getElementById('pt'),pn=document.getElementById('pn'),pd=document.getElementById('pd'),pr=document.getElementById('pr');
let sel=-1,drag=false,moved=0,lx=0,vel=0,tgt=0,focus=false,mx=0,my=0;
D.forEach((e,i)=>{const b=document.createElement('button');b.textContent=e.id;b.onclick=()=>pick(i);chips.appendChild(b)});
document.getElementById('x').onclick=()=>pick(-1);
const wp=new THREE.Vector3();
function pick(i){
 sel=i;[...chips.children].forEach((b,j)=>b.classList.toggle('on',j===i));
 if(i<0){panel.style.display='none';return}
 const e=D[i],hex='#'+nc[i].getHexString();
 pt.textContent=e.s;pn.textContent=e.n;pd.textContent=e.d;pr.textContent=e.r;panel.style.setProperty('--glow',hex);
 panel.style.display='block';panel.classList.remove('in');void panel.offsetWidth;panel.classList.add('in');
 const m=nodes[i];tgt=-Math.atan2(m.position.z,m.position.x)+Math.PI/2;
 let d=tgt-G.rotation.y;d=Math.atan2(Math.sin(d),Math.cos(d));tgt=G.rotation.y+d;focus=true;
 m.getWorldPosition(wp);wave(wp,C[e.k]);
}
const ray=new THREE.Raycaster(),ptr=new THREE.Vector2();
R.domElement.addEventListener('pointerdown',e=>{drag=true;moved=0;lx=e.clientX;focus=false});
addEventListener('pointerup',e=>{
 if(drag&&moved<5&&e.target===R.domElement){
  ptr.set(e.clientX/innerWidth*2-1,-(e.clientY/innerHeight)*2+1);ray.setFromCamera(ptr,cam);
  const h=ray.intersectObjects(nodes,false)[0];
  if(h)pick(h.object.userData.i);else{pick(-1);wave(new THREE.Vector3(),0x5BC0BE)}
 }drag=false});
addEventListener('pointermove',e=>{
 mx=e.clientX/innerWidth-.5;my=e.clientY/innerHeight-.5;
 if(drag){const dx=e.clientX-lx;lx=e.clientX;moved+=Math.abs(dx);vel=dx*.006;G.rotation.y+=vel}
});
addEventListener('resize',()=>{cam.aspect=innerWidth/innerHeight;cam.updateProjectionMatrix();R.setSize(innerWidth,innerHeight)});
const clk=new THREE.Clock();
(function loop(){
 requestAnimationFrame(loop);const dt=Math.min(clk.getDelta(),.05),t=clk.elapsedTime;
 if(!drag){
  if(focus)G.rotation.y+=(tgt-G.rotation.y)*.06;
  else{vel*=.95;G.rotation.y+=vel+(sel<0?.003:0)}
 }
 knot.rotation.x=t*.25;knot.rotation.y=t*.35;knot.scale.setScalar(1+Math.sin(t*1.6)*.06);
 coreGlow.material.opacity=.4+Math.sin(t*1.6)*.12;
 stars.rotation.y=t*.01;if(!reduce)gal.rotation.y=t*.02;
 nodes.forEach(m=>{const u=m.userData;m.rotation.y=t*.6+u.i;m.position.y=u.base+Math.sin(t*1.2+u.i)*.15;
  const k=Math.min(1,Math.max(0,(t-u.born)/.9)),intro=1+2.7*Math.pow(k-1,3)+1.7*Math.pow(k-1,2);
  const ts=u.i===sel?1.5:1;u.s+=(ts-u.s)*.1;m.scale.setScalar(Math.max(.001,u.s*(k>=1?1:intro)))});
 E.forEach(([a,b],k)=>{const A=nodes[a].position,B=nodes[b].position,on=sel<0||a===sel||b===sel;
  ew[k]+=((on?1:.12)-ew[k])*.08;const w=ew[k];
  lp.set([A.x,A.y,A.z,B.x,B.y,B.z],k*6);
  lc.set([nc[a].r*w*.55,nc[a].g*w*.55,nc[a].b*w*.55,nc[b].r*w*.55,nc[b].g*w*.55,nc[b].b*w*.55],k*6);
  for(let j=0;j<3;j++){const ph=(t*.22+j/3+k*.17)%1,o=(k*3+j)*3,f=Math.sin(Math.PI*ph)*w;
   pp[o]=A.x+(B.x-A.x)*ph;pp[o+1]=A.y+(B.y-A.y)*ph;pp[o+2]=A.z+(B.z-A.z)*ph;
   pcl[o]=nc[b].r*f;pcl[o+1]=nc[b].g*f;pcl[o+2]=nc[b].b*f}});
 lg.attributes.position.needsUpdate=true;lg.attributes.color.needsUpdate=true;pg.attributes.position.needsUpdate=true;pg.attributes.color.needsUpdate=true;
 for(let i=waves.length-1;i>=0;i--){const w=waves[i];w.t+=dt;w.m.scale.setScalar(1+w.t*14);w.m.material.opacity=Math.max(0,.9*(1-w.t/1.4));if(w.t>1.4){S.remove(w.m);w.m.geometry.dispose();w.m.material.dispose();waves.splice(i,1)}}
 cam.position.x+=(mx*3-cam.position.x)*.04;cam.position.y+=(2.5-my*2-cam.position.y)*.04;cam.position.z+=((sel>=0?11.5:14)-cam.position.z)*(t<2.5&&!reduce?.03:.05);cam.lookAt(0,0,0);
 R.render(S,cam);
})();
</script>
</body>
</html>
