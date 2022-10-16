import numpy as np
import open3d as o3d

N = 500000

mesh = o3d.io.read_triangle_mesh(r"C:\Users\jayan\Downloads\export.gltf")
# mesh2 = copy.deepcopy(mesh)
pcd = mesh.sample_points_poisson_disk(N)
# fit to unit cube
pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
          center=pcd.get_center())
pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
o3d.visualization.draw_geometries([pcd])

voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                            voxel_size=0.05)
o3d.visualization.draw_geometries([voxel_grid])

print('octree division')
octree = o3d.geometry.Octree(max_depth=9)
octree.create_from_voxel_grid(voxel_grid)
o3d.visualization.draw_geometries([octree])
