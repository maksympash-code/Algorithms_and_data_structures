def solve():
    import sys
    # Зчитування вхідних даних (без numpy)
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        N = int(next(it))
        M = int(next(it))
    except StopIteration:
        return

    # Для кожної зупинки зчитуємо:
    # - час руху від зупинки i до зупинки i+1
    # - кількість робітників K та їх час приходу (у неспадному порядку)
    stops = [None] * N  # для кожної зупинки – список часів приходу робітників
    travel = [0] * N    # travel[i] – час руху від зупинки i до i+1
    total_workers = 0
    max_arrival = 0  # максимальний час приходу серед усіх робітників
    for i in range(N):
        t = int(next(it))
        travel[i] = t
        k = int(next(it))
        total_workers += k
        workers = [0] * k
        for j in range(k):
            val = int(next(it))
            workers[j] = val
        stops[i] = workers
        if k > 0 and workers[-1] > max_arrival:
            max_arrival = workers[-1]
    # Цільова кількість перевезених робітників – це min(total_workers, M)
    target = M if total_workers >= M else total_workers

    # Якщо робітників немає, автобус просто рухається за маршрутом
    totalTravel = sum(travel)
    if target == 0:
        sys.stdout.write(str(totalTravel))
        return

    # --- Компресія зупинок ---
    # Об’єднуємо послідовні зупинки, на яких немає робітників,
    # оскільки там немає вибору – автобус просто рухається далі.
    comp_stops = []
    comp_travel = []
    accum = 0
    for i in range(N):
        if not stops[i]:  # зупинка порожня
            accum += travel[i]
        else:
            if accum:
                comp_stops.append([])  # компресована зупинка без робітників
                comp_travel.append(accum + travel[i])
                accum = 0
            else:
                comp_stops.append(stops[i])
                comp_travel.append(travel[i])
    if accum:
        comp_stops.append([])
        comp_travel.append(accum)
    n = len(comp_stops)
    totalTravel_comp = sum(comp_travel)
    # Обчислюємо масив rem для компресованих зупинок:
    # rem[i] = comp_travel[i] + comp_travel[i+1] + ... + comp_travel[n-1]
    rem = [0] * (n + 1)
    rem[n] = 0
    for i in range(n - 1, -1, -1):
        rem[i] = comp_travel[i] + rem[i + 1]

    INF = 10**18

    # --- Функція перевірки feasible(T) ---
    # Ми використовуємо динамічне програмування:
    # dp[r] – мінімальний час від’їзду з попередньої зупинки (на компресованому маршруті),
    # якщо до цього вже забрано r робітників.
    #
    # На кожній зупинці з індексом i дозволено чекати не пізніше L = T - rem[i].
    # Якщо автобус приїхав на зупинку у час A, то:
    #   - якщо x робітників вже чекають (тобто, їхній час приходу ≤ A), час від’їзду залишається A;
    #   - інакше – потрібно чекати до прибуття x–го робітника, тобто час стає worker[x-1].
    # Ми оновлюємо dp для нового стану: dp[r+x] = min(dp[r+x], candidate)
    def feasible(T):
        dp = [0] + [INF] * target  # dp[0] = 0, інші – INF
        # Проходимо по компресованих зупинках: i = 0 .. n-1
        for i in range(n):
            L = T - rem[i]  # останній допустимий час від’їзду з цієї зупинки
            newdp = [INF] * (target + 1)
            # Визначаємо час прибуття: для i==0 offset = 0, для i>0 – offset = comp_travel[i-1]
            if i == 0:
                offset = 0
            else:
                offset = comp_travel[i - 1]
            st = comp_stops[i]  # список часів приходу робітників на зупинці i
            k = len(st)
            # Перебір станів dp (кількість робітників, забраних до цієї зупинки)
            for r in range(target + 1):
                cur = dp[r]
                if cur == INF:
                    continue
                A = cur + offset  # час прибуття на зупинку i
                if A > L:
                    continue  # занадто пізно – не можемо чекати на цій зупинці
                # Варіант: не брати жодного робітника – стан залишається r, час = A
                if A < newdp[r]:
                    newdp[r] = A
                if k == 0:
                    continue  # якщо на зупинці немає робітників, переходимо далі
                # Знаходимо j – кількість робітників, що вже приїхали (час ≤ A)
                lo_b = 0
                hi_b = k
                while lo_b < hi_b:
                    mid = (lo_b + hi_b) >> 1
                    if st[mid] <= A:
                        lo_b = mid + 1
                    else:
                        hi_b = mid
                j = lo_b
                # Максимальна кількість робітників, яких можна забрати з цієї зупинки
                avail = target - r
                if avail > k:
                    avail = k
                # Для x = 1 .. avail – вибір посадити x робітників
                # Якщо x ≤ j, час від’їзду залишається A; інакше – потрібно чекати до st[x-1]
                # Якщо candidate > L, подальші x не розглядаємо
                local_st = st  # локальна змінна для пришвидшення
                local_A = A
                local_newdp = newdp
                for x in range(1, avail + 1):
                    if x <= j:
                        cand = local_A
                    else:
                        cand = local_st[x - 1]
                    if cand > L:
                        break
                    idx = r + x
                    if cand < local_newdp[idx]:
                        local_newdp[idx] = cand
            dp = newdp
        # Після останньої зупинки автобус проїжджає останній відрізок – це comp_travel[n-1]
        final_time = dp[target] + comp_travel[n - 1]
        return final_time <= T

    # --- Бінарний пошук по відповіді ---
    # Мінімально можливий час – коли автобус не чекає: totalTravel_comp.
    # Максимально можливий – totalTravel_comp + max_arrival (якщо потрібно чекати на пізньо прибуваючого робітника)
    lo = totalTravel_comp
    hi = totalTravel_comp + max_arrival
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    sys.stdout.write(str(ans))


if __name__ == '__main__':
    solve()
