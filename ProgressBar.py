import datetime, sys

start = datetime.datetime.now()

def print_progress_bar (iteration, total):

    process_duration_samples = []
    average_samples = 5

    end = datetime.datetime.now()

    process_duration = end - start

    if len(process_duration_samples) == 0:
        process_duration_samples = [process_duration] * average_samples

    process_duration_samples = process_duration_samples[1:average_samples-1] + [process_duration]
    average_process_duration = sum(process_duration_samples, datetime.timedelta()) / len(process_duration_samples)
    remaining_steps = total - iteration
    remaining_time_estimation = remaining_steps * average_process_duration

    bars_string = int(float(iteration) / float(total) * 20.)
    sys.stdout.write(
        "\r[%-20s] %d%% (%s/%s) Estimated time left: %s" % (
            '█'*bars_string, float(iteration) / float(total) * 100,
            iteration,
            total,
            remaining_time_estimation
        ) 
    )
    sys.stdout.flush()
    if iteration + 1 == total:
        print 