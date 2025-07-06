import os
import argparse

def generate_ini_files(template_path, output_dir, param_name, start, stop, step):
    # Load the base ini template
    with open(template_path, 'r') as file:
        template = file.read()

    os.makedirs(output_dir, exist_ok=True)

    # Generate ini files with different parameter values
    for value in range(start, stop + 1, step):
        modified = template.replace(f"{param_name}=default", f"{param_name}={value}")
        output_path = os.path.join(output_dir, f"{param_name}_{value}.ini")
        with open(output_path, 'w') as f:
            f.write(modified)
        print(f"✅ Created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--template', type=str, default='Backtests/template.ini', help='Path to base .ini file')
    parser.add_argument('--output_dir', type=str, default='Backtests/configs', help='Directory to save generated .ini files')
    parser.add_argument('--param', type=str, default='RSI_Period', help='Parameter name to vary')
    parser.add_argument('--start', type=int, default=5, help='Start value of parameter')
    parser.add_argument('--stop', type=int, default=15, help='Stop value of parameter')
    parser.add_argument('--step', type=int, default=2, help='Step size')

    args = parser.parse_args()

    generate_ini_files(args.template, args.output_dir, args.param, args.start, args.stop, args.step)
