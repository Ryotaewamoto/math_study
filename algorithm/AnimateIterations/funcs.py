import numpy as np

def Animate3D(fun, x0_min,x0_max, x1_min, x1_max, x0_vals, x1_vals,f_vals):
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import animation

    X,Y = np.meshgrid(np.linspace(x0_min,x0_max,100), np.linspace(x1_min,x1_max,100))
    zs = np.array(fun([np.ravel(X), np.ravel(Y)]))
    Z = zs.reshape(X.shape)

    fig = plt.figure(figsize=(7,7))
    ax = Axes3D(fig)

    ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap='jet', alpha=0.5)

    ax.set_xlabel('$x_0$')
    ax.set_ylabel('$y_0$')
    ax.set_zlabel('$f(x_0,x_1)$')
    ax.view_init(45, -45)

    # Create animation
    line, = ax.plot([], [], [], 'purple', label='path', lw=1.5)
    point, = ax.plot([], [], [], '*', color='purple')
    display_value = ax.text(2., 2., 27.5, '', transform=ax.transAxes)

    def init_2():
        line.set_data([], [])
        line.set_3d_properties([])
        point.set_data([], [])
        point.set_3d_properties([])
        display_value.set_text('')

        return line, point
    
    def animate_2(i):
        # Animate line
        line.set_data(x0_vals[:i], x1_vals[:i])
        line.set_3d_properties(f_vals[:i])

        # Animate point
        point.set_data(x0_vals[i], x1_vals[i])
        point.set_3d_properties(f_vals[i])

        return line, point, display_value
    
    ax.legend(loc =1)

    anim2 = animation.FuncAnimation(fig, animate_2, init_func=init_2, frames=len(x0_vals), interval=120, repeat_delay=60, blit=True)

    plt.show(anim2)

def Animate2D(fun, x0_min,x0_max, x1_min, x1_max, x0_vals, x1_vals):

    from matplotlib import pyplot as plt
    from matplotlib import animation

    X,Y = np.meshgrid(np.linspace(x0_min,x0_max,100), np.linspace(x1_min,x1_max,100))
    zs = np.array(fun([np.ravel(X), np.ravel(Y)]))
    Z = zs.reshape(X.shape)

    fig, ax = plt.subplots(figsize=(7,7))
    ax.contour(X, Y, Z, 100, cmap='jet')

    line, = ax.plot([], [], 'purple', label='path', lw=1.5)
    point, = ax.plot([], [], '*', color='purple', markersize=4)
    value_display = ax.text(0.02, 0.02, '', transform=ax.transAxes)

    def init_1():
        line.set_data([], [])
        point.set_data([], [])
        value_display.set_text('')

        return line, point, value_display

    def animate_1(i):
        # Animate line
        line.set_data(x0_vals[:i], x1_vals[:i])
        
        # Animate point
        point.set_data(x0_vals[i], x1_vals[i])

        return line, point, value_display
    
    ax.legend(loc =1)

    anim1 = animation.FuncAnimation(fig, animate_1, init_func=init_1, frames=len(x0_vals), interval=100, repeat_delay=60, blit=True)

    plt.show(anim1)
