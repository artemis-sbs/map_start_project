import random
from sbs_utils.procedural.spawn import terrain_spawn
from sbs_utils.procedural.ship_data import plain_asteroid_keys
from sbs_utils import scatter
import random



def test_spawn_asteroid_box(x,y,z, size_x=10000,size_z=None, density_scale=1.0, density=1, height=1000):
    """
        density is per 1000. Defaults to 0.5.
    """
    if density_scale==0:
        return
    if size_z is None:
        size_z = size_x
    
    grid = size_x/1000 + size_z/1000
    amount = max(int(grid * density), 1)
    amount = random.randrange(int(amount/2), int(amount* density_scale))
    
    cluster_spawn_points = scatter.box(amount,  x + size_x/2, -height/2, z+size_z/2, size_x, height/2, size_z, True, 0, 0, 0 )
    test_spawn_asteroid_scatter(cluster_spawn_points, height)


def test_spawn_asteroid_sphere(x,y,z, radius=10000, density_scale=1.0, density=1, height=1000):
    if density_scale==0:
        return
    grid = radius/1000
    grid = grid + grid

    amount = max(int(grid * density), 1)
    amount = random.randrange(int(amount* density_scale))

    cluster_spawn_points = scatter.sphere(amount,  x, y,z, radius)
    test_spawn_asteroid_scatter(cluster_spawn_points, height)


def test_spawn_asteroid_scatter(cluster_spawn_points, height):
    asteroid_types = plain_asteroid_keys()
    a_type = random.choice(asteroid_types)

    er = 1
    scatter_pass = 0
    for v2 in cluster_spawn_points:
        v2.y = v2.y % (height/2)
        a_type = random.choice(asteroid_types)

        asteroid = terrain_spawn(v2.x, v2.y, v2.z,None, "#,asteroid", a_type, "behav_asteroid")
        asteroid.engine_object.steer_yaw = random.uniform(0.0001, 0.003)
        asteroid.engine_object.steer_pitch = -random.uniform(0.0001, 0.003)
        asteroid.engine_object.steer_roll = random.uniform(0.0001, 0.003)

        # Some big, some small
        # big are more spherical
        # 1 in 4 big
        er = asteroid.engine_object.exclusion_radius
        moons = False
        if scatter_pass%4 == 0:
            sx = random.uniform(7.0, 15.0)
            sy = sx + random.uniform(-1.2, 1.2)
            sz = sx + random.uniform(-1.2, 1.2)
            sm = min(sx, sy)
            sm = min(sm, sz)
            er *= sm/2
            asteroid.engine_object.exclusion_radius = er
            moons = True
        else:
            sx = random.uniform(2.5, 5)
            sy = random.uniform(2.5, 5)
            sz = random.uniform(2.5, 5)
            sm = min(sx, sy)
            sm = min(sm, sz)
            #moons = random.randint(0,3)!=2
            

        scatter_pass += 1
        #er = asteroid.blob.get("exclusionradius",0)
        #er *= sm

        asteroid.blob.set("local_scale_x_coeff", sx)
        asteroid.blob.set("local_scale_y_coeff", sy)
        asteroid.blob.set("local_scale_z_coeff", sz)
        
        # Big asteroids
        if not moons:
            continue
            # #
        # else:
        #     continue

        # #
        # # Sphere od smaller asteroids
        # #
        this_amount = random.randint(4,10)
        
        little = scatter.sphere(this_amount,  v2.x, 0,v2.z, er + 50, er + 100 )
        #little = scatter.sphere(random.randint(2,6), v2.x, v2.y, v2.z, 300, 800)
        # little = scatter.sphere(random.randint(12,26), v2.x, v2.y, v2.z, 800)
        
        for v3 in little: 
            a_type = random.choice(asteroid_types)

            asteroid = terrain_spawn(v3.x, v3.y, v3.z,None, "#,asteroid", a_type, "behav_asteroid")
            asteroid.engine_object.steer_yaw = random.uniform(0.0001, 0.003)
            asteroid.engine_object.steer_pitch = -random.uniform(0.0001, 0.003)
            asteroid.engine_object.steer_roll = random.uniform(0.0001, 0.003)
            sx1 = random.uniform(0.3, 1.0)
            sy1 = random.uniform(0.3, 1.0)
            sz1 = random.uniform(0.3, 1.0)
            sm1 = max(sx, sy)
            sm1 = max(sm, sz)
            # er = asteroid.engine_object.exclusion_radius
            # er *= sm1
            asteroid.engine_object.exclusion_radius = 1
            

            asteroid.blob.set("local_scale_x_coeff", sx1)
            asteroid.blob.set("local_scale_y_coeff", sy1)
            asteroid.blob.set("local_scale_z_coeff", sz1)



def test_spawn_nebula_box(x,y,z, size_x=10000, size_z=None, density_scale=1.0, density= 0.25, height=1000):
    if density_scale==0:
        return
    if size_z is None:
        size_z = size_x
    
    grid = size_x/1000 + size_z/1000
    amount = max(int(grid * density), 1)
    amount = random.randrange(int(amount/2), int(amount* density_scale))

    cluster_spawn_points = scatter.box(amount,  x + size_x/2, -height/2, z+size_z/2, size_x, height/2, size_z, True, 0, 0, 0 )
    test_spawn_nebula_common(cluster_spawn_points, height)

def test_spawn_nebula_sphere(x,y,z, radius=10000, density_scale=1.0, density=0.25, height=1000):
    if density_scale==0:
        return
    
    grid = radius/1000 + radius/1000
    amount = max(int(grid * density), 1)
    amount = random.randrange(int(amount* density_scale))
    
    cluster_spawn_points = scatter.sphere(amount, x, y, z, radius)
    test_spawn_nebula_common(cluster_spawn_points, height)


def test_spawn_nebula_common(cluster_spawn_points, height):
    for v2 in cluster_spawn_points:
        v2.y = v2.y % (height/2)
        nebula = terrain_spawn(v2.x, v2.y, v2.z,None, "#, nebula", "nebula", "behav_nebula")
        nebula.blob.set("local_scale_x_coeff", random.uniform(1.0, 5.5))
        nebula.blob.set("local_scale_y_coeff", random.uniform(1.0, 5.5))
        nebula.blob.set("local_scale_z_coeff", random.uniform(1.0, 5.5))

